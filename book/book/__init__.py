from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "ASDFAS123SS@SDaf234$#%"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/log_book'
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"

# Register the blueprints
from book.routes.home import home_bp
from book.routes.user import user_bp
from book.routes.logbook import logbook_bp

app.register_blueprint(home_bp)
app.register_blueprint(user_bp)
app.register_blueprint(logbook_bp)

