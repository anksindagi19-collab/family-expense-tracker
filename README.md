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
- ☁️ Deployed on Render

---

## 🏗️ Project Structure

```text
Family-Expense-Tracker/
│── app.py                 # Main Flask application
│── models.py              # Database models
│── config.py              # Application configuration
│── requirements.txt       # Project dependencies
│── Procfile               # Gunicorn configuration for Render
│── runtime.txt            # Python runtime version
│── README.md
│
├── templates/
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_income.html
│   ├── add_expense.html
│   ├── view_expenses.html
│   └── tracker.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── expense_tracker.db
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

```text
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
7. Delete expenses when needed.
8. Logout securely.
9. Each user can only access their own financial data.

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
- Render

---

# 🌐 Live Demo

### 🚀 Live Website

👉 **https://family-expense-tracker-8oaw.onrender.com**

---

# 💻 GitHub Repository

👉 **https://github.com/anksindagi19-collab/family-expense-tracker**

---

# 🔮 Future Improvements

- 🔐 Password Hashing
- 📅 Monthly Reports
- 📊 Expense Charts & Graphs
- 📂 Export Reports (PDF / Excel)
- 🔍 Filter by Date & Category
- 🏷️ Expense Categories
- 📱 Mobile-Friendly UI
- 📧 Email Notifications
- ☁️ PostgreSQL Database Integration

---


# 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Developed By

**Ankita Sindagi**

Electronics & Communication Engineering (ECE)

**GitHub:** https://github.com/anksindagi19-collab

**Live Demo:** https://family-expense-tracker-8oaw.onrender.com
