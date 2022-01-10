from finviz.screener import Screener
import pandas as pd
filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
stock_list = Screener()  # Get the performance table and sort it by price ascending

# Export the screener results to .csv
stock_list.to_csv('ender.csv')
# Create a SQLite database
stock_list.to_sqlite("stock.sqlite3")

for stock in stock_list[9:19]:  # Loop through 10th - 20th stocks
    print(stock['Ticker'], stock['Price']) # Print symbol and price

# Add more filters
df = pd.read_csv('ender.csv')

#for i in range(0,len(df)):
#    if df['Market Cap'].astype(str).str[-4:].str.contains('B'):
 #       print()

mcap = df[df['Market Cap'].astype(str).str[-4:].str.contains('B') & df['Country'].astype(str).str[-4:].str.contains('USA') and df[df['P/E'] > 20]]
print(mcap)
#print(df.loc[df['P/E'] != '-'])
# Print the table into the console
#print(stock_list)