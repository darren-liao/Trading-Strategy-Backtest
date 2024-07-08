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

        self.order = None

    def notify_order(self, order): 
        if order.status in [order.Submitted, order.Accepted]: 
            return 
        
        elif order.status in [order.Completed]:  
            if order.isbuy(): 
                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, order.executed.price))
            elif order.issell(): 
                print("Sell {} shares of {} at {}".format(self.size, self.params.ticker,order.executed.price))

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:  
            print("Order failed") 

        self.order = None     

    def next(self):  
        if self.order: 
            return  
        
        elif self.position.size == 0: #only buy if we do not already hold a position 
            if self.crossover > 0: #Golden Cross - 50 day SMA crosses above 200 day SMA 
                self.size = math.floor(self.broker.get_cash() / self.data.close) 
                self.buy(size = self.size) 

        elif self.position.size > 0: 
            if self.crossover < 0: #Death Cross - 50 day SMA crosses below 200 day SMA 
                self.close() 