import csv
from datetime import datetime

class FinanceTracker:
    def __init__(self, filename='data.csv'):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

    def add_transaction(self, amount, category, description=""):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append([date, amount, category, description])
        self.save_transactions()

    def save_transactions(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.transactions)

    def get_summary(self):
        income = sum(float(t[1]) for t in self.transactions if float(t[1]) > 0)
        expenses = sum(float(t[1]) for t in self.transactions if float(t[1]) < 0)
        balance = income + expenses
        return {'income': income, 'expenses': expenses, 'balance': balance}