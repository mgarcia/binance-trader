# -*- coding: UTF-8 -*-
# @guldenpt

from multiprocessing import Pool
import sys
import random
import time
from config_coins import COINS
import copy

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
    pair_config = {
        "symbol": "TODO",
        "quantity": 0,
        "profit": 1.33,
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
    pairs = Orders.get_pairs()
    coins = {}
    coins_market = COINS.keys()
    for pair, pair_info in pairs.iteritems():
        coin_market = pair_info["quoteAsset"]
        if coin_market in coins_market:
          new_pair_config = copy.deepcopy(pair_config)
          new_pair_config.update(COINS[coin_market])
          new_pair_config["symbol"] = pair
          coins[pair] = new_pair_config

    pool_size = len(coins)
    pool = Pool(pool_size)
    args = [Struct(**coins[pair]) for pair in coins]
    pool.map(run_trade, args)

