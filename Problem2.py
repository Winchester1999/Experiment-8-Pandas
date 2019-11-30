# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:05:21 2019

@author: Wency
"""

import pandas as pd
Cars = pd.read_csv('cars.csv')
rows = Cars.iloc[0:5:,range(0,11,2)]
mazda = Cars.loc[Cars['Model'] == 'Mazda RX4']
camaro = Cars.loc[Cars['Model'] == 'Camaro Z28', ['Model','cyl']]
gear1 = Cars.loc[Cars['Model'] == 'Mazda RX4 Wag', ['Model','cyl','gear']]
gear2 = Cars.loc[Cars['Model'] == 'Ford Pantera L', ['Model','cyl','gear']]
gear3 = Cars.loc[Cars['Model'] == 'Honda Civic', ['Model','cyl','gear']]
print("A.", rows)
print(" ")
print("B.", mazda)
print(" ")
print("C.", camaro)
print(" ")
print("D.", gear1)
print(gear2)
print(gear3)