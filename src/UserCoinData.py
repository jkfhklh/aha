# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:54:09 2017

@author: Zifan
"""

import CoinData

class UserCoinData(CoinData.CoinData):
    
    def __init__(self,name,price=0,base="RMB",amount=0,platform="wallet"):
        CoinData.CoinData.__init__(self,name,price,base)
        self.amount = amount
        self.platform = platform
        