# reporting.py
import pandas as pd

def generate_monthly_summary():
    df = pd.read_csv('data.csv', names=['Date', 'Amount', 'Category', 'Description'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    monthly_summary = df.resample('M').sum()
    print(monthly_summary)

# Example usage
if __name__ == "__main__":
    generate_monthly_summary()
