from datetime import date
from tabulate import tabulate


def add_expense(expenses: list[dict]) -> None:

    print("\nAdd a new Expense")

    amount_str = input("Amount(e.g., 120.50)").strip()
    category = input("Category (e.g., travel/food/rent)").strip()
    description = input("Description (e.g., uber auto/ swiggy)").strip()

    if not amount_str:
        print("Error!:- Amount cannot be empty.")
        return
    
    try:
        amount = float(amount_str)
    except ValueError:
        print("Error!:- Amount must be a number.")
        return

    if amount <= 0:
        print("Error!:- Amount must be greater than 0.")
        return

    if not category:
        print("Error!:- Category cannot be empty.")
        return
    
    expense = {
        "date" : str(date.today()),
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def list_expenses(expenses: list[dict]) ->None:
    print("\nAll expenses.")

    if not expenses:
        print("No expenses found.")
        return
    
    rows = []
    for e in expenses:
        rows.append([e["date"], e["amount"], e["category"], e["description"]])

    print(tabulate(rows, headers=["Date", "Amount", "Category", "Description"], tablefmt= "grid"))


def show_total(expenses: list[dict]) ->None:
    total = 0.0
    for e in expenses:
        total += float(e["amount"])
    
    print(f"\nTotal Spending = {total:.2f}")

def show_category_summary(expenses: list[dict]) ->None:
    print("\nCategory Summary.")

    if not expenses:
        print("No Expenses found yet.")
        return
    
    summary = {}
    for e in expenses:
        cat = e["category"]
        amt = e["amount"]
        summary[cat] = summary.get(cat, 0.0) + amt

    rows = []
    for cat, amt in summary.items():
        rows.append([cat, f"₹{amt:.2f}"])

    print(tabulate(rows, headers=["Category", "Total"], tablefmt="grid"))

    
    

