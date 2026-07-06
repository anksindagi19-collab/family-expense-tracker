# 💰 Family Expense Tracker

Family Expense Tracker is a Flask-based web application that helps users manage their personal income and expenses. Each user has a secure account where they can record income, track expenses, and view a financial summary without seeing other users' data.

---

## 🚀 Features

- 👤 User Registration & Login
- 🔐 Session-Based Authentication
- 💵 Add Monthly Income
- 📝 Add Daily Expenses
- 📋 View Personal Expense History
- 🗑️ Delete Expenses
- 📊 Financial Summary Dashboard
- 👥 Multi-User Support (Each user can access only their own data)
- 💾 SQLite Database Integration
- 🌐 Live Web Application

---

## 🏗️ Project Structure

```
Family-Expense-Tracker/
│── app.py                 # Main Flask application
│── models.py              # Database models
│── config.py              # Application configuration
│── requirements.txt       # Project dependencies
│── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_income.html
│   ├── add_expense.html
│   ├── view_expenses.html
│   └── tracker.html
│
│── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
│── expense_tracker.db     # SQLite Database
│── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anksindagi19-collab/family-expense-tracker.git
cd family-expense-tracker
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 💡 How It Works

1. Register a new account.
2. Login using your email and password.
3. Add your monthly income.
4. Record your daily expenses.
5. View your expense history.
6. Check your financial summary.
7. Logout securely.
8. Each user can only access their own financial data.

---

# 📊 Financial Summary

The application automatically calculates:

- ✅ Total Income
- ✅ Total Expenses
- ✅ Remaining Balance

---

# 🛠️ Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML5
- CSS3
- Git
- GitHub
- PythonAnywhere

---

# 🌐 Live Demo

**Live Website**

👉 https://ankitasindagi.pythonanywhere.com

---

# 💻 GitHub Repository

👉 https://github.com/anksindagi19-collab/family-expense-tracker

---

# 🔮 Future Improvements

- 🔐 Password Hashing
- 📅 Monthly Reports
- 📊 Expense Charts & Graphs
- 📂 Export Reports (PDF / Excel)
- 🔍 Filter by Date & Category
- 📱 Mobile-Friendly UI
- 📧 Email Notifications
- 🌍 Cloud Database Integration

---

# 📸 Screenshots

_Add screenshots of your Home Page, Dashboard, Add Expense, View Expenses, and Financial Summary here._

---

# 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Developed By

**Ankita Sindagi**

Electronics & Communication Engineering (ECE)

GitHub: https://github.com/anksindagi19-collab
