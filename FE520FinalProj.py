#FE 520
#Final Project

import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt

jpm = pdr.get_data_yahoo('JPM',
                          start=datetime.datetime(2009, 1, 1),
                          end=datetime.datetime(2019, 1, 1))
#JP  Morgan
pnc = pdr.get_data_yahoo('PNC',
                          start=datetime.datetime(2009, 1, 1),
                          end=datetime.datetime(2019, 1, 1))
#PNC Bank
db = pdr.get_data_yahoo('DB',
                          start=datetime.datetime(2009, 1, 1),
                          end=datetime.datetime(2019, 1, 1))
#Deutsche Bank
wfc = pdr.get_data_yahoo('WFC',
                          start=datetime.datetime(2009, 1, 1),
                          end=datetime.datetime(2019, 1, 1))
#Wells Fargo
bac = pdr.get_data_yahoo('BAC',
                          start=datetime.datetime(2009, 1, 1),
                          end=datetime.datetime(2019, 1, 1))
#Bank of America



# Plot the closing prices for `bac
bac['Close'].plot(grid=True)

# Show the plot
plt.show()

# Isolate the adjusted closing prices
adj_close_px = bac['Adj Close']

# Short moving window rolling mean
bac['42'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean
bac['252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
bac[['Adj Close', '42', '252']].plot()

# Show plot
plt.show()





