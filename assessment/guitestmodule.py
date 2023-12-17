## Data collection and visualisation

import yfinance as yf
import pandas as pd
from pandas import  read_csv
from pandas import set_option
from matplotlib import pyplot as plt
# %matplotlib inline
import matplotlib.dates as mpl_dates
from datetime import date, timedelta

import plotly.offline as py
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

plt.style.use('seaborn-darkgrid')

#### Data Engineering

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1

df = pd.DataFrame()

crypto_ticker = ['BTC']



#Extract data for each of the 10 coins from YahooFinance! using a For loop.
for each_crypto_ticker in crypto_ticker:

    each_crypto_ticker_index = crypto_ticker.index(each_crypto_ticker)
    crypto_data = yf.Ticker(f"{each_crypto_ticker}-USD").history(start='2015-01-01', end=end_date, interval='1d')
    crypto_dataframe = pd.DataFrame(crypto_data)
    crypto_dataframe['crypto_ticker'] = each_crypto_ticker
    df = pd.concat([df, crypto_dataframe])


set_option('display.width', 500)
df = df.rename_axis('cryptodate').reset_index()

# ###Convert data to CSV and store it
df.to_csv("soligencecryptodata_withdate.csv")

###Extract data to different dataframes to simplify data understanding for each cryptocurrency
BTC = df.loc[df['crypto_ticker'] == 'BTC']

layout = go.Layout(paper_bgcolor='rgba(223,201,230,0)', plot_bgcolor='rgba(0,0,0,0)')
figure = go.Figure(data=[go.Candlestick(x=df["cryptodate"],open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"])],layout=layout)
figure.update_layout(title = "Bitcoin Price Analysis", xaxis_rangeslider_visible=True)
figure.show()