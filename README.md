💰 My Expense Tracker CLI 💰
Hey there! 👋

Welcome to your personal finance sidekick—a simple, yet powerful, Command-Line Interface (CLI) expense tracker. With this app, you can easily log and manage all your spending directly from your terminal. No complicated interfaces, just a straightforward way to keep your wallet in check. All your expense data is saved securely in a local JSON file.

Let's see what it can do!

🧐 Features: What's in It?
This app is designed to be your quick, go-to solution for tracking money. It comes packed with essential features:

Add an Expense: Quickly add a new expense with a description and amount. It automatically adds the current date for you.

View a List: Get a complete list of all your recorded expenses, neatly displayed with their ID, date, description, and amount.

Get a Summary: Want to know where you stand? Get a summary of your total spending. You can also filter this summary to see your total expenses for a specific month.

Update an Expense: Made a mistake? No problem. You can easily update the description or amount of any expense by its unique ID.

Delete an Expense: If a transaction was recorded by mistake, you can remove it forever.

🛠️ How to Use It?
Running this app is super simple. Just make sure you have Python 3 installed on your system.

1. Run the Commands
All the magic happens with a single command. Just open your terminal in the same directory as your expense_tracker.py file and run the following commands:

To Add an Expense:

python expense_tracker.py add --description "Coffee" --amount 2.50
# Output: Expense added successfully (ID: 1)

To View All Expenses:

python expense_tracker.py list

To Get a Total Summary:

python expense_tracker.py summary

To Get a Summary for a Specific Month (e.g., August):

python expense_tracker.py summary --month 8

To Update an Expense:

python expense_tracker.py update --id 1 --description "Morning Coffee with a friend" --amount 5.00

To Delete an Expense:

python expense_tracker.py delete --id 1

📝 Expense Properties: The Inside Scoop
Each expense is a JSON object with the following properties:

id: A unique number that identifies each expense.

date: The date the expense was recorded.

description: A short description of what you spent money on.

amount: The amount of money spent.

https://roadmap.sh/projects/expense-tracker