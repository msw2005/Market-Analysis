import yfinance as yf

# Download data from the web
ticker = yf.Ticker("AAPL")

# Get info data
info = ticker.info


'''
The time period for these metrics is determined by Yahoo Finance, which provides the data. The "trailing" in "trailing P/E" and "trailing EPS" typically means
these metrics are calculated using data from the past 12 months.
'''
# Get the metrics
pe_ratio = info.get('trailingPE')
eps = info.get('trailingEps')

# Print metrics
print(f"P/E Ratio: {pe_ratio}")
print(f"EPS: {eps}")
