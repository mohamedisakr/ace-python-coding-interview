import csv
from os import path
from csv import reader, writer
from collections import defaultdict
from datetime import datetime
from transaction import Transaction

# '''
# const [transactions, setTransactions] = useState([
#     { id: 1, date: '2024-03-30', category: 'Groceries', amount: 120.50, type: 'expense' },
#     { id: 2, date: '2024-03-29', category: 'Salary', amount: 3000.00, type: 'income' },
#     { id: 3, date: '2024-03-28', category: 'Utilities', amount: 95.20, type: 'expense' },
#     { id: 4, date: '2024-03-27', category: 'Entertainment', amount: 50.00, type: 'expense' },
#   ]);

#   const [budgets, setBudgets] = useState([
#     { category: 'Groceries', limit: 500, spent: 320.50 },
#     { category: 'Entertainment', limit: 200, spent: 150.00 },
#     { category: 'Utilities', limit: 300, spent: 95.20 },
#     { category: 'Transportation', limit: 250, spent: 180.30 },
#   ]);

#   // Calculate total income and expenses
#   const totalIncome = transactions
#     .filter(t => t.type === 'income')
#     .reduce((sum, t) => sum + t.amount, 0);

#   const totalExpenses = transactions
#     .filter(t => t.type === 'expense')
#     .reduce((sum, t) => sum + t.amount, 0);

#   // Prepare data for the spending breakdown chart
#   const spendingByCategory = transactions
#     .filter(t => t.type === 'expense')
#     .reduce((acc, t) => {
#       acc[t.category] = (acc[t.category] || 0) + t.amount;
#       return acc;
#     }, {});
# '''


def load_from_file(file_name='budget.csv'):
    transaction_list = []
    file_path = path.join(path.dirname(__file__), file_name)
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                if len(row) != 4:
                    raise ValueError(f"Invalid row format: {row}")
                date, category, amount, description = row
                try:
                    amount = float(amount)
                except ValueError:
                    raise ValueError(f"Invalid amount: {amount}")
                transaction_list.append(Transaction(
                    date, category, amount, description))
        return transaction_list
    except FileNotFoundError:
        print("No existing budget file found.")
    except IOError as e:
        raise OSError(f"File operation failed: {e}")


def calculate_total_income(transaction_list):
    return sum(trans.amount for trans in transaction_list if trans.description == 'income')


def calculate_total_expenses(transaction_list):
    return sum(trans.amount for trans in transaction_list if trans.description == 'expense')


def calculate_spending_by_category(transaction_list):
    spending_dict = defaultdict(float)

    expenses = filter(lambda t: t.description == 'expense', transaction_list)

    for trans in expenses:
        spending_dict[trans.category] += trans.amount

    return dict(spending_dict)


transactions = load_from_file()
spending = calculate_spending_by_category(transactions)
print(spending)

# transactions = load_from_file()
# total_expenses = calculate_total_expenses(transactions)
# print(total_expenses)

# transactions = load_from_file()
# total_income = calculate_total_income(transactions)
# print(total_income)

# transactions = load_from_file()
# # print(transactions)


# for transaction in transactions:
#     print(transaction)
#     # You can also access individual attributes like this:
#     print(f"Date: {transaction.date}")
#     print(f"Category: {transaction.category}")
#     print(f"Amount: {transaction.amount}")
#     print(f"Description: {transaction.description}")
#     print("----------")
