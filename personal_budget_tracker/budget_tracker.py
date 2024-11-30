import csv
from os import path
from csv import reader, writer
from collections import defaultdict
# import matplotlib.pyplot as plt
from datetime import datetime
from transaction import Transaction


class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.categories = ['Food', 'Transport', 'Utilities', 'Entertainment']

    def add_transaction(self, date, category, amount, description):
        transaction = Transaction(date, category, amount, description)
        self.transactions.append(transaction)

    def view_transactions(self):
        for t in self.transactions:
            print(f"Date: {t.date}, Category: {t.category}, Amount: ${
                  t.amount:.2f}, Description: {t.description}")

    def save_to_file(self, file_name='budget.csv'):
        file_path = path.join(path.dirname(__file__), file_name)
        try:
            with open(file_path, 'w', newline='') as file:
                csv_writer = writer(file)
                csv_writer.writerow(
                    ['Date', 'Category', 'Amount', 'Description'])
                for t in self.transactions:
                    csv_writer.writerow(
                        [t.date, t.category, t.amount, t.description])
        except IOError as e:
            raise OSError(f"File operation failed: {e}")

    def load_from_file(self, file_name='budget.csv'):
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
                    self.transactions.append(Transaction(
                        date, category, amount, description))
        except FileNotFoundError:
            print("No existing budget file found.")
        except IOError as e:
            raise OSError(f"File operation failed: {e}")

    def category_summary(self):
        summary = defaultdict(float)
        for t in self.transactions:
            summary[t.category] += t.amount
        print("\nCategory Summary:")

        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

    def monthly_report(self, year, month):
        monthly_total = 0
        print(f"\nTransactions for {year}-{month}")

        for t in self.transactions:
            t_date = datetime.strptime(t.date, '%Y-%m-%d')
            if t_date.year == int(year) and t_date.month == int(month):
                print(f"- {t.description}: ${t.amount:.2f}")
                monthly_total += t.amount

        print(f"Total: ${monthly_total:.2f}")

    def add_recurring_transaction(self, transaction, frequency):
        # Add code for recurring transactions
        pass

    def generate_future_projections(self, months):
        # Project future balance based on recurring transactions
        pass

    def export_report(self, format_type='pdf'):
        # Add code to export reports in different formats
        pass
