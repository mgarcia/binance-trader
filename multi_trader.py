# -*- coding: UTF-8 -*-
# @guldenpt

from multiprocessing import Pool
import sys
import random
import time
from config_coins import COINS

sys.path.insert(0, './app')

from Orders import Orders
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
  t = Trading(option, Orders)
  t.run()

if __name__ == '__main__':
    pool_size = len(COINS)
    pool = Pool(pool_size)
    args = [Struct(**COINS[pair]) for pair in COINS]
    pool.map(run_trade, args)

