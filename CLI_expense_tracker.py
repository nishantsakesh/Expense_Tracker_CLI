import argparse
import json
import os
from datetime import datetime

# Define the file name for storing expenses
EXPENSES_FILE = 'expenses.json'

def load_expenses():
    """
    Loads expenses from the JSON file. Creates an empty file if it doesn't exist.
    """
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """
    Saves the list of expenses to the JSON file.
    """
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(args):
    """
    Adds a new expense to the tracker.
    """
    expenses = load_expenses()
    
    # Validate amount
    try:
        amount = float(args.amount)
        if amount <= 0:
            print("Error: Amount must be a positive number.")
            return
    except ValueError:
        print("Error: Invalid amount. Please provide a number.")
        return

    # Generate a unique ID
    expense_id = 1
    if expenses:
        expense_id = max(e['id'] for e in expenses) + 1

    new_expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": args.description,
        "amount": amount,
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

def update_expense(args):
    """
    Updates an existing expense by its ID.
    """
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if expense['id'] == args.id:
            # Update description if provided
            if args.description:
                expense['description'] = args.description
            # Update amount if provided
            if args.amount:
                try:
                    amount = float(args.amount)
                    if amount <= 0:
                        print("Error: Amount must be a positive number.")
                        return
                    expense['amount'] = amount
                except ValueError:
                    print("Error: Invalid amount. Please provide a number.")
                    return
            found = True
            break
    
    if found:
        save_expenses(expenses)
        print(f"Expense with ID {args.id} updated successfully.")
    else:
        print(f"Error: Expense with ID {args.id} not found.")

def delete_expense(args):
    """
    Deletes an expense by its ID.
    """
    expenses = load_expenses()
    initial_count = len(expenses)
    
    # Filter out the expense to be deleted
    expenses = [e for e in expenses if e['id'] != args.id]
    
    if len(expenses) < initial_count:
        save_expenses(expenses)
        print(f"Expense deleted successfully (ID: {args.id}).")
    else:
        print(f"Error: Expense with ID {args.id} not found.")

def list_expenses(args):
    """
    Lists all expenses.
    """
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    print("ID  Date       Description     Amount")
    print("--------------------------------------")
    for expense in expenses:
        print(f"{expense['id']:<3} {expense['date']:<10} {expense['description']:<15} ${expense['amount']:.2f}")

def summary_expenses(args):
    """
    Provides a summary of expenses, either total or for a specific month.
    """
    expenses = load_expenses()
    total_expenses = 0
    
    if args.month:
        month_str = f"{datetime.now().year}-{int(args.month):02d}"
        monthly_expenses = [e for e in expenses if e['date'].startswith(month_str)]
        total_expenses = sum(e['amount'] for e in monthly_expenses)
        month_name = datetime(2024, int(args.month), 1).strftime("%B")
        print(f"Total expenses for {month_name}: ${total_expenses:.2f}")
    else:
        total_expenses = sum(e['amount'] for e in expenses)
        print(f"Total expenses: ${total_expenses:.2f}")

def main():
    """
    Main function to handle command-line arguments.
    """
    parser = argparse.ArgumentParser(description="A simple command-line expense tracker.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command parser
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', required=True, help='Amount of the expense')

    # Update command parser
    update_parser = subparsers.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('--id', type=int, required=True, help='ID of the expense to update')
    update_parser.add_argument('--description', help='New description of the expense')
    update_parser.add_argument('--amount', help='New amount of the expense')

    # Delete command parser
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')

    # List command parser
    list_parser = subparsers.add_parser('list', help='List all expenses')

    # Summary command parser
    summary_parser = subparsers.add_parser('summary', help='Get a summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Summary for a specific month (e.g., 8 for August)')

    args = parser.parse_args()

    if args.command == 'add':
        add_expense(args)
    elif args.command == 'update':
        update_expense(args)
    elif args.command == 'delete':
        delete_expense(args)
    elif args.command == 'list':
        list_expenses(args)
    elif args.command == 'summary':
        summary_expenses(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
