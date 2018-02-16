# -*- coding: UTF-8 -*-
# @yasinkuyu
import config 

from BinanceAPI import BinanceAPI
from Messages import Messages

# Define Custom import vars
client = BinanceAPI(config.api_key, config.api_secret)

class Stats():
 
    @staticmethod
    def get_weightedAvgPrice(symbol):
        try:

            kline = client.get_kline(symbol)
            ticker = client.get_ticker(symbol)
            print kline
            print ticker
    
        except Exception as e:
            print ('ob: %s' % (e))
            return None
