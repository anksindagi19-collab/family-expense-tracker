from flask import Flask, render_template, request, redirect
from config import Config
from models import db, User, Expense, Income

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            username=username,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- ADD INCOME ----------------

@app.route("/add_income", methods=["GET", "POST"])
def add_income():

    if request.method == "POST":

        source = request.form["source"]
        amount = request.form["amount"]

        income = Income(
            source=source,
            amount=amount
        )

        db.session.add(income)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("add_income.html")


# ---------------- ADD EXPENSE ----------------

@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        title = request.form["title"]
        amount = request.form["amount"]
        category = request.form["category"]

        expense = Expense(
            title=title,
            amount=float(amount),
            category=category
        )

        db.session.add(expense)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("add_expense.html")

# ---------------- VIEW EXPENSES ----------------

@app.route("/view_expenses")
def view_expenses():

    expenses = Expense.query.all()

    return render_template(
        "view_expenses.html",
        expenses=expenses
    )


# ---------------- DELETE EXPENSE ----------------

@app.route("/delete_expense/<int:id>")
def delete_expense(id):

    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    return redirect("/view_expenses")


# ---------------- FINANCIAL SUMMARY ----------------

@app.route("/tracker")
def tracker():

    incomes = Income.query.all()
    expenses = Expense.query.all()

    total_income = sum(income.amount for income in incomes)

    total_expense = sum(expense.amount for expense in expenses)

    balance = total_income - total_expense

    return render_template(
        "tracker.html",
        incomes=incomes,
        expenses=expenses,
        total_income=total_income,
        total_expense=total_expense,
        balance=balance
    )


# ---------------- RUN APP ----------------

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)