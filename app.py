from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
###pip install flask_sqlalchemy, flask_login
##https://sqlitebrowser.org/dl/

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecretkey"

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#Insert data into db
conn = sqlite3.connect('instance/db.sqlite')
cursor = conn.cursor()

users = [
    ('Jane', generate_password_hash('123')),
    ('Mike', generate_password_hash('456')),
    ('alice', generate_password_hash('123')),
    ('bob', generate_password_hash('123'))
]
cursor.executemany('INSERT OR IGNORE INTO user (username, password) VALUES (?, ?)', users)
conn.commit()
conn.close()

#create User model
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(250), unique = True, nullable = False)
  password = db.Column(db.String(250), nullable = False)

# Create database
with app.app_context():
  db.create_all()

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
    # if user and check_password_hash(user.password, password):
      login_user(user)
      return render_template('index.html', user=current_user)
    else:
      return render_template('login.html', error = "Invalid username or password")
    
  return render_template("login.html")      


@app.route('/register')
def register():
  return render_template('register.html')


@app.route('/logout')
def logout():
  return render_template('logout.html')


if __name__ == '__main__':
  app.run(debug=True)
