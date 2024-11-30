from csv import reader, writer
from collections import defaultdict
import matplotlib.pyplot as plt
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
            print(f"Date: {t.date}, Category: {t.category}")
            print(f"Amount: ${t.amount:.2f}")
            print(f"Description: {t.description}\n")

    def save_to_file(self):
        with open('budget.csv', 'w', newline='') as file:
            csv_writer = writer(file)
            csv_writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            for t in self.transactions:
                csv_writer.writerow(
                    [t.date, t.category, t.amount, t.description])

    def load_from_file(self):
        try:
            with open('budget.csv', 'r') as file:
                csv_reader = reader(file)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    transaction = Transaction(
                        row[0], row[1], float(row[2]), row[3])
                    self.transactions.append(transaction)
        except FileNotFoundError:
            print("No existing budget file found.")

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
            t_year, t_month = t.date.split('-')[:2]

            if t_year == year and t_month == month:
                print(f"- {t.description}: ${t.amount:.2f}")
                monthly_total += t.amount

        print(f"Total: ${monthly_total:.2f}")

    # PHASE 6: Data Visualization (Week 5)
    def create_visualizations(self):
        # Pie chart of spending by category
        categories = [t.category for t in self.transactions]
        amounts = [t.amount for t in self.transactions]

        plt.figure(figsize=(10, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title('Spending by Category')
        plt.show()

        # Monthly spending trend
        # Add trend line visualization here

    # PHASE 7: Advanced Features (Week 6)
    # 1. Recurring Transactions:
    def add_recurring_transaction(self, transaction, frequency):
        # Add code for recurring transactions
        pass

    def generate_future_projections(self, months):
        # Project future balance based on recurring transactions
        pass

    # 2. Export Reports:
    def export_report(self, format_type='pdf'):
        # Add code to export reports in different formats
        pass
