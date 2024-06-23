import pandas as pd 
import backtrader as bt 
from strategies.golden_cross import golden_cross 

cerebro = bt.Cerebro() 

cerebro.broker.setcash(100000)  

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True) 

feed = bt.feeds.PandasData(dataname = spy_prices) 

cerebro.adddata(feed) 

cerebro.addstrategy(golden_cross)

cerebro.run() 
cerebro.plot()