import csv

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("\n📊 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(STOCK_PRICES.keys()))
print("Type 'done' to finish input.\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in STOCK_PRICES:
        print("❌ Stock not available. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.\n")
            continue
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("✅ Stock added successfully.\n")

print("\n📈 Portfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    price = STOCK_PRICES[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock} | Quantity: {qty} | Value: ${investment}")

print("-" * 30)
print(f"💰 Total Investment Value: ${total_investment}")

# Save to TXT file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-" * 30 + "\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} - Quantity: {qty}, Price: ${STOCK_PRICES[stock]}\n")
    file.write(f"\nTotal Investment: ${total_investment}")

# Save to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
    for stock, qty in portfolio.items():
        writer.writerow([stock, qty, STOCK_PRICES[stock], qty * STOCK_PRICES[stock]])

print("\n📁 Portfolio saved as portfolio.txt and portfolio.csv")
print("✅ Thank you for using Stock Portfolio Tracker!")
