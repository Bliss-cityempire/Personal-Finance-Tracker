import csv
from datetime import datetime

def add_transaction(date, amount, category, description):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

# Example usage
transactions = [
    ('2024-08-15', 100.50, 'Food', 'Dinner at restaurant'),
    ('2024-08-16', -50.00, 'Utilities', 'Electric bill'),
    ('2024-08-17', 200.00, 'Income', 'Freelance project payment'),
    ('2024-08-18', -75.00, 'Rent', 'Monthly apartment rent'),
    ('2024-08-19', -20.00, 'Transportation', 'Bus fare'),
    ('2024-08-20', 150.00, 'Income', 'Bonus received'),
    ('2024-08-21', -10.00, 'Entertainment', 'Movie ticket'),
]

for transaction in transactions:
    add_transaction(*transaction)
