from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from book.models import LogBook, LogEntry
from book import db

logbook_bp = Blueprint('logbook', __name__)


@logbook_bp.route('/logbooks/create', methods=['GET', 'POST'])
@login_required
def create_logbook():
    if request.method == 'POST':
        name = request.form['name']
        variable_type = request.form['variable_type']
        logbook = LogBook(name=name, variable_type=variable_type, user_id=current_user.id)
        db.session.add(logbook)
        db.session.commit()
        return redirect(url_for('home.home'))
    return render_template('logbook/create_logbook.html')


@logbook_bp.route('/logbooks/<int:logbook_id>/edit', methods=['GET', 'POST'])
def edit_logbook(logbook_id):
    logbook = LogBook.query.get(logbook_id)
    if request.method == 'POST':
        logbook.name = request.form['name']
        logbook.variable_type = request.form['variable_type']
        db.session.commit()
        flash('Logbook updated successfully!', 'success')
        return redirect(url_for('home.home'))

    return render_template('logbook/edit_logbook.html', logbook=logbook)

@logbook_bp.route('/logbook/<int:logbook_id>/delete', methods=['GET', 'POST'])
def delete_logbook(logbook_id):
    logbook = LogBook.query.get(logbook_id)

    if logbook:
        # delete first all log entires associated with this log book
        LogEntry.query.filter_by(logbook_id=logbook.id).delete()

        # delete log book itself
        db.session.delete(logbook)
        db.session.commit()
        flash('Logbook deleted successfully.', 'success')
        return jsonify({'success': True})
    else:
        flash('Logbook not found.', 'danger')
        return jsonify({'success': False})


@logbook_bp.route('/logbook/<int:logbook_id>/entries', methods=['GET', 'POST'])
def logbook_entries(logbook_id):
    logbook = LogBook.query.get(logbook_id)
    if not logbook:
        return redirect(url_for('home.home'))
    
    if request.method == 'POST':
        log_value = request.form['log_value']
        
        if logbook.variable_type == 'int':
            try:
                log_value = int(log_value)
            except ValueError:
                flash('Invalid log value. Please enter an integer.', 'danger')
                return redirect(url_for('logbook.logbook_entries', logbook_id=logbook_id))
        elif logbook.variable_type == 'double':
            try:
                log_value = float(log_value)
            except ValueError:
                flash('Invalid log value. Please enter a valid number.', 'danger')
                return redirect(url_for('logbook.logbook_entries', logbook_id=logbook_id))
        elif logbook.variable_type == 'string':
            if not isinstance(log_value, str):
                flash('Invalid log value. Please enter a valid string.', 'danger')
                return redirect(url_for('logbook.logbook_entries', logbook_id=logbook_id))
        
        entry = LogEntry(logbook_id=logbook_id, log_value=log_value)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('logbook.logbook_entries', logbook_id=logbook_id))
    
    entries = LogEntry.query.filter_by(logbook_id=logbook_id).order_by(LogEntry.id.desc()).all()
    return render_template('logbook/logbook_entries.html', logbook=logbook, entries=entries)

@logbook_bp.route('/logbook/<int:logbook_id>/entries/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(logbook_id, entry_id):
    entry = LogEntry.query.get_or_404(entry_id)
    if request.method == 'POST':
        entry.log_value = request.form['log_value']
        db.session.commit()
        return redirect(f'/logbook/{logbook_id}/entries')

    return render_template('logbook/logbook_entries.html', entry=entry)

@logbook_bp.route('/logbook/<int:logbook_id>/entries/<int:entry_id>/delete', methods=['POST'])
def delete_entry(logbook_id, entry_id):
    entry = LogEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(f'/logbook/{logbook_id}/entries')
