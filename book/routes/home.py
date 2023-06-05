from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, current_user
from book.models import LogBook

home_bp = Blueprint('home',__name__)


@home_bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('home.home'))

@home_bp.route('/home')
@login_required
def home():
    logbooks = LogBook.query.filter_by(user_id=current_user.id).order_by(LogBook.id.desc()).all()
    return render_template('logbook/home.html',logbooks=logbooks)
