import backtrader as bt 
import math  

class golden_cross(bt.Strategy): 
    params = (
        ('fast', 50), 
        ('slow', 200), 
        ('ticker', 'SPY')) 

    def __init__(self): 
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, 
            period=self.params.fast, 
            plotname='50 day moving average'
        ) 

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, 
            period=self.params.slow, 
            plotname='200 day moving average'
        ) 

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, 
            self.slow_moving_average
        ) 

    def next(self): 
        if self.position.size == 0: #only buy if we do not already hold a position 
            if self.crossover > 0: #Golden Cross - 50 day SMA crosses above 200 day SMA 

                self.size = math.floor(self.broker.get_cash() / self.data.close) 

                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.buy(size = self.size) 

        elif self.position.size > 0: 
            if self.crossover < 0: #Death Cross - 50 day SMA crosses below 200 day SMA
                print("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))

                self.close()