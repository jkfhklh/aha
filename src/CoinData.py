# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:47:22 2017

@author: Zifan
"""

class CoinData:
    ID = 0
    
    def __init__(self,name,price=0,base="RMB"):
        self.name = name
        self.price = price
        self.base = base
        CoinData.ID += 1
        self.id = CoinData.ID