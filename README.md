# Flask Login App

This project is a simple login web application built with Flask. It demonstrates user registration, login, and password hashing using modern Python libraries.

## Tech Stack & Libraries

- **Python 3**
- **Flask**: Web framework
- **Flask-Login**: User session management
- **Flask-SQLAlchemy**: ORM for database operations
- **Werkzeug**: For password hashing
- **SQLite**: Lightweight database (file-based)

## Setup & Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/JaneCS2025/Flask-Log-in-App.git
   cd app1
   ```

2. **Create a virtual environment (optional but recommended)**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install flask flask_sqlalchemy flask_login
   ```

4. **Run the application**
   ```sh
   python app.py
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Main Steps to Create a Login App in Flask

1. **Set up Flask and configuration**
2. **Define the User model with SQLAlchemy**
3. **Initialize Flask-Login and user loader**
4. **Create registration and login routes**
5. **Hash passwords using Werkzeug**
6. **Store user data in SQLite**
7. **Create HTML templates for login, register, and home**
8. **Run and test the app locally**

## Notes

- Passwords are securely hashed before storing in the database.
- You can customize templates in the `templates/` folder.
- The database file is located at `instance/db.sqlite`.

---

Feel free to fork and extend this project!
Flask App Screenshot:

4 different routs in the app:
http://127.0.0.1:5000 </br>
http://127.0.0.1:5000/login  </br>
http://127.0.0.1:5000/register  </br>
http://127.0.0.1:5000/logout  </br>

 </br>
<img width="602" height="244" alt="Screenshot 2026-02-11 at 11 14 56 AM" src="https://github.com/user-attachments/assets/b0949c4c-c36b-45bd-977a-5d5208de383c" />

