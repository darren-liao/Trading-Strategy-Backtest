import backtrader as bt  
import math 

class buy_hold(bt.Strategy):  

    def __init__(self): 
        pass 

    def next(self): 
        if self.position.size == 0: 
            self.size = math.floor(self.broker.get_cash() / self.data.close) 
            self.buy(size = self.size)