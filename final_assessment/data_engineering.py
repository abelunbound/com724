## I changed data type of SP500 from int64 to datetime64[ns] using     sp500['date'] = pd.to_datetime(sp500['date'])
## This is because webscraping exercise brought back the data as an integer