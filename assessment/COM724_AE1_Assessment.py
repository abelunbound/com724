##Data Collection and Storage

###Import relevant libraries

import yfinance as yf
import pandas as pd
from pandas import  read_csv
from pandas import set_option
from matplotlib import pyplot as plt

###Import live data from YahooFinance! API and Store in a dataframe
#Create an empty pandas dataframe
df = pd.DataFrame()

#Create a list with all crypto symbols. Use top 10 coins by market capitalisation according to CoinGecko.com
crypto_ticker = ['BTC', 'ETH', 'USDT', 'USDC', 'BNB', 'BUSD', 'XRP', 'ADA', 'SOL', 'DOGE']

#Extract data for each of the 10 coins from YahooFinance! using a For loop.
for each_crypto_ticker in crypto_ticker:
    each_crypto_ticker_index = crypto_ticker.index(each_crypto_ticker)
    crypto_data = yf.Ticker(f"{each_crypto_ticker}-USD").history(start='2019-01-01', end='2022-06-30', interval='1d')
    crypto_dataframe = pd.DataFrame(crypto_data)
    crypto_dataframe['crypto_ticker'] = each_crypto_ticker
    df = pd.concat([df, crypto_dataframe])

df.to_csv("soligencecryptodata.csv")

###Extract data to different dataframes to simplify data understanding for each cryptocurrency
BTC_crypto_data = df.loc[df['crypto_ticker'] == 'BTC']
ETH_crypto_data = df.loc[df['crypto_ticker'] == 'ETH']
USDT_crypto_data = df.loc[df['crypto_ticker'] == 'USDT']
USDC_crypto_data = df.loc[df['crypto_ticker'] == 'USDC']
BNB_crypto_data = df.loc[df['crypto_ticker'] == 'BNB']
BUSD_crypto_data = df.loc[df['crypto_ticker'] == 'BUSD']
XRP_crypto_data = df.loc[df['crypto_ticker'] == 'XRP']
ADA_crypto_data = df.loc[df['crypto_ticker'] == 'ADA']
SOL_crypto_data = df.loc[df['crypto_ticker'] == 'SOL']
DOGE_crypto_data = df.loc[df['crypto_ticker'] == 'DOGE']


###Twitter and other Social media sentiment?

##Data Understanding
print("\n-----Data Profile-----\n")
print(df.shape)
print(df.dtypes)

print("\n-----Statistical Analysis-----\n")
print(BTC_crypto_data.describe())

BTC_crypto_data.hist()
plt.tight_layout()
plt.show()



#Data Preprocessing
print("\n-----Missing Values-----\n")
print(df.isna().sum())
