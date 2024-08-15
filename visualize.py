import matplotlib.pyplot as plt
import csv
from collections import defaultdict

def plot_expenses():
    categories = {}
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[2]
            amount = float(row[1])
            if amount < 0:  # Only consider expenses
                if category in categories:
                    categories[category] += -amount
                else:
                    categories[category] = -amount

    plt.figure(figsize=(10, 7))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Expense Categories')
    plt.show()

def plot_expenses_vs_income():
    dates = []
    incomes = []
    expenses = []

    # Read data from CSV
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date = row[0]
            amount = float(row[1])
            dates.append(date)
            if amount > 0:
                incomes.append(amount)
                expenses.append(0)
            else:
                incomes.append(0)
                expenses.append(-amount)

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(dates, incomes, label='Income', color='green')
    plt.plot(dates, expenses, label='Expenses', color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income vs. Expenses Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
