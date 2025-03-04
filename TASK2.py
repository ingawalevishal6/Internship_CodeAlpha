import pandas
import yfinance as yf
from prettytable import PrettyTable


# Portfolio dictionary to store stock symbols and number of shares
portfolio = {}


def add_stock(symbol, shares):
    """Add a stock to the portfolio"""
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol}.")

def remove_stock(symbol):
    """Remove a stock from the portfolio"""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from the portfolio.")
    else:
        print("Stock not found in portfolio.")

def display_portfolio():
    """Fetch and display real-time stock data"""
    if not portfolio:
        print("Portfolio is empty.")
        return
    
    table = PrettyTable(["Stock", "Shares", "Price", "Total Value"])
    
    total_portfolio_value = 0
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1]
        total_value = shares * price
        table.add_row([symbol, shares, f"${price:.2f}", f"${total_value:.2f}"])
        total_portfolio_value += total_value
    
    print(table)
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")

def main():
          print("Thise portfolio only support for Apple company")
    while True:
         
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter stock name (e.g., aapl): ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(name, shares)
        
        elif choice == "2":
            name = input("Enter stock symbol to remove: ").upper()
            remove_stock(name)
        
        elif choice == "3":
            display_portfolio()
        
        elif choice == "4":
            print("Exiting... Thank you!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
