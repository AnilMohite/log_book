from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, logout_user
from book.models import User
from book import db, login_manager

user_bp = Blueprint('user', __name__)


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

# =============== routes ====================


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            db.session.add(user)
            db.session.commit()
            flash('Logged in successfully!', 'success')
            next_url = request.args.get('next', None)
            if next_url:
                session['next_url'] = next_url
            return redirect(url_for('home.home'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('user.login'))

    return render_template('user/login.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User with the same email already exists.', 'danger')
            return redirect(url_for('user.register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        try:
            user = User(email=email, name=name, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully!', 'success')
            return redirect(url_for('home.home'))
        except Exception as e:
            flash('Failed to create user: {}'.format(str(e)), 'danger')
      
    return render_template('user/register.html')

@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')
