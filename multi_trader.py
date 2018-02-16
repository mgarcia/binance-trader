# -*- coding: UTF-8 -*-
# @guldenpt

from multiprocessing import Pool
import sys
import random
import time


sys.path.insert(0, './app')

from Trading import Trading
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)      

# Function to allow multi arguments for pool multiprocessing
# Ref: https://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments#answer-21130146
def multi_run_wrapper(args):
    return run_trade(*args)

def run_trade(option):
  timeDelay = random.randrange(0, 5)
  time.sleep(timeDelay)
  t = Trading(option)
  t.run()

if __name__ == '__main__':
    trades = {
            "ADXETH": {
                "symbol": "ADXETH",
                "quantity": 15,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
            "NEOETH": {
                "symbol": "NEOETH",
                "quantity": 0.09,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
            "BCCETH": {
                "symbol": "BCCETH",
                "quantity": 0.007,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
		},
            "LTCETH": {
                "symbol": "LTCETH",
                "quantity": 0.043,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
            "TRXETH": {
                "symbol": "TRXETH",
                "quantity": 2,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
           "XRPETH": {
                "symbol": "XRPETH",
                "quantity": 9,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
           "XLMETH": {
                "symbol": "XLMETH",
                "quantity": 24,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                },
           "ETCETH": {
                "symbol": "ETCETH",
                "quantity": 0.29,
                "profit": 1.2,
		"amount": 0,
                "max_amount": False,
                "stop_loss": 0,
                "increasing": 0.2,
                "decreasing": 0.2,
                "orderid": 0,
                "wait_time": 20,
                "test_mode": False,
                "prints": True,
                "debug": True,
                "loop": 0,
                "max_buyprice": 0,
                "spread_threshold": 1,
                "mode": "profit",
                "buyprice": 0,
                "sellprice": 0
                }



 
            }
     
    pool = Pool()
    args = [Struct(**trades[pair]) for pair in trades]
    pool.map(run_trade, args)

