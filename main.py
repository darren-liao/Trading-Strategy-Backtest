import pandas as pd 
import backtrader as bt  

from strategies.golden_cross import golden_cross  
from strategies.buy_hold import buy_hold 
from strategies.sma import SMAStrategy

cerebro = bt.Cerebro() 

cerebro.broker.setcash(100000)  

spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True) 

feed = bt.feeds.PandasData(dataname = spy_prices) 

cerebro.adddata(feed) 

#pick the strategy you want to test

cerebro.addstrategy(golden_cross)
#cerebro.addstrategy(buy_hold) 

cerebro.run() 
cerebro.plot()