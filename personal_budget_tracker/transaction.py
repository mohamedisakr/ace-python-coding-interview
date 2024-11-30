from datetime import datetime


class Transaction:
    def __init__(self, date, category, amount, description):
        # Validate the date
        try:
            datetime.strptime(
                date, "%Y-%m-%d") or datetime.strptime(date, "%Y/%m/%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date}")

        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


# def add_transaction(self):
#     date = input("Enter date (YYYY-MM-DD): ")
#     category = input("Enter category: ")
#     amount = float(input("Enter amount: "))
#     description = input("Enter description: ")

# transaction = Transaction(date, category, amount, description)
# self.transactions.append(transaction)
