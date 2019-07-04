# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:31:42 2019

@author: rizwa
"""
import pandas as pd
import numpy as np
import random as rand

Products_dict = {'P01':['Carnival de Tapas',16], 'P02':['Fritura de Cangrejo',10], 'P03':['Yuca Frita con Mojo Cubano', 11], 
                 'P04':['Camarones al ajillo', 8], 'P05':['Bon bon de pollo', 9], 'P06':['Chorizo', 10], 'P07':['Mariquitas', 9],
                'P08':['Maduros Fritos', 7], 'P09':['Cigar del Pinar',8], 'P10':['Calamares', 10], 'P11':['Quesadillas',9], 'P12':['Tortilla Mambo',10],
                'P13':['Queso de Cabra', 9], 'P14':['Ropa Vieja',8], 'P15':['Masas de Lechon Fritas', 12]}

def discountCheck():
    pass

def price_calculator(x):
    totalAmount = 0
    for items in x:
        totalAmount = totalAmount + int(Products_dict[items][1])
    return totalAmount

def dataGenerator():
    date_rng =  pd.date_range(start = '1/1/2017', end = '5/5/2019', freq = 'H')
    dataFrame = pd.DataFrame(data = date_rng, columns = ['Date_Time'], index = date_rng)
    dataFrame = pd.DataFrame(data = dataFrame, index = date_rng).between_time('11:30', '23:30')
    dataFrame['Date of Arrival'] = [d.date() for d in dataFrame['Date_Time']]
    dataFrame['Time of Arrival'] = [d.time() for d in dataFrame['Date_Time']]
    dataFrame['Month'] = pd.to_datetime(dataFrame['Date of Arrival'].astype(str)).dt.month.astype(int)
    dataFrame['Day'] = pd.to_datetime(dataFrame['Date of Arrival'].astype(str)).dt.day.astype(int)
    dataFrame['Hour'] = pd.to_datetime(dataFrame['Time of Arrival'].astype(str)).dt.hour.astype(int)
    dataFrame['Week'] = dataFrame['Day'].map(lambda x : int(np.ceil(x/7)))
    #dataFrame['Items_Ordered'] = dataFrame['Time of Arrival'].map(lambda x : rand.sample(population=list(Products_dict.keys()), k=rand.randint(2,8)))
    #dataFrame['Discount(Boolean)'] = dataFrame['Day'].map(lambda x : rand.choice([True, False]))
    #dataFrame['Discount(Boolean)'].where 
    dataFrame['Group of People'] = dataFrame['Time of Arrival'].map(lambda x : rand.randint(1,6))
    dataFrame['Items_Ordered'] = dataFrame['Group of People'].apply(lambda x : rand.sample(population=list(Products_dict.keys()), k=rand.randint(x,int(x)+4)))
    dataFrame['Total Amount'] = dataFrame['Items_Ordered'].map(lambda x:price_calculator(x) )
    

    
