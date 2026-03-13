# Flask Login App

This project is a simple login web application built with Flask. It demonstrates user registration, login, and password hashing using modern Python libraries. It also includes Gen AI integration to provide personalized welcome messages based on user information.

## Tech Stack & Libraries

- **Python 3**
- **Flask**: Web framework
- **Flask-Login**: User session management
- **Flask-SQLAlchemy**: ORM for database operations
- **Werkzeug**: For password hashing
- **SQLite**: Lightweight database (file-based)
- **Google Generative AI (Gemini)**: For personalized welcome messages
- **python-dotenv**: For environment variable management

## Setup & Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/JaneCS2025/Flask-Log-in-App.git
   cd app1
   ```

2. **Create a virtual environment (optional but recommended)**
   For windows command:

   ```sh
   python3 -m venv venv
   venv\Scripts\activate (windows)
   source venv/bin/activate (mac)
   ```

3. **Install dependencies**

   ```sh
   pip install flask flask_sqlalchemy flask_login python-dotenv google-generativeai
   ```

## Gen AI Setup (Google Gemini)

### Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click on **"Create API Key"**
3. Select your Google Cloud Project (or create a new one)
4. Copy the API key

### Step 2: Create `.env` File

Create a `.env` file in the project root directory:

```sh
touch .env
```

### Step 3: Add Your API Key to `.env`

Open the `.env` file and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

**Example:**

```
GEMINI_API_KEY=12345...
```

⚠️ **Important**: Never commit the `.env` file to version control! It's already in `.gitignore`.

### Step 4: Verify Setup

Run the app and check if the API key is loaded correctly:

```sh
python app.py
```

If you see errors about missing API key, ensure:

- `.env` file exists in the project root
- `GEMINI_API_KEY` is set correctly without `export` keyword
- The format is: `KEY=VALUE` (no spaces around `=`)

### Step 5: Install Gen AI Package:

-`pip install google-generativeai` 
-`pip install python-dotenv`

## How Gen AI Works in This App

1. **User Registration**: When a user registers, they select a hobby from the dropdown
2. **User Login**: After successful login, the user is redirected to a personalized welcome page
3. **AI Welcome Message**: The app uses Google Gemini AI to generate a personalized welcome message based on the user's hobby and other profile information
4. **Dynamic Content**: Each user sees a unique welcome message tailored to their interests

## Available Gemini Models

The app uses `gemini-2.5-flash` by default, but you can switch to other models:

- **`gemini-2.5-flash`** (Recommended) - Fast and efficient
- **`gemini-1.5-pro`** - More powerful for complex tasks
- **`gemini-1.5-flash`** - Previous version, lighter weight

To change the model, edit `ai_service.py`:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",  # Change model here
    contents=prompt
)
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

4 different routs in the app: </br>
http://127.0.0.1:5000 </br>
http://127.0.0.1:5000/login </br>
http://127.0.0.1:5000/register </br>
http://127.0.0.1:5000/logout </br>

 </br>
<img width="602" height="244" alt="Screenshot 2026-02-11 at 11 14 56 AM" src="https://github.com/user-attachments/assets/b0949c4c-c36b-45bd-977a-5d5208de383c" />
