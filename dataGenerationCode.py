# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:31:42 2019

@author: rizwa
"""
import pandas as pd
import numpy as np
import random as rand
import datetime

Products_dict = {'P01':['Carnival de Tapas',16], 'P02':['Fritura de Cangrejo',10], 'P03':['Yuca Frita con Mojo Cubano', 11], 
                 'P04':['Camarones al ajillo', 8], 'P05':['Bon bon de pollo', 9], 'P06':['Chorizo', 10], 'P07':['Mariquitas', 9],
                'P08':['Maduros Fritos', 7], 'P09':['Cigar del Pinar',8], 'P10':['Calamares', 10], 'P11':['Quesadillas',9], 'P12':['Tortilla Mambo',10],
                'P13':['Queso de Cabra', 9], 'P14':['Ropa Vieja',8], 'P15':['Masas de Lechon Fritas', 12]}

Table_numbers = {1 : ['T01','T02','T03','T04','T05','T06','T07','T08','T09','T10'], 2 : ['T01','T02','T03','T04','T05','T06','T07','T08','T09','T10']
                 ,3 : ['T05','T06','T07','T08','T09','T10'] ,4 : ['T05','T06','T07','T08','T09','T10'], 
                 5 :['T09','T10'], 6: ['T09','T10']}

def discountCheck():
    pass

def price_calculator(x):
    totalAmount = 0
    for items in x:
        totalAmount = totalAmount + int(Products_dict[items][1])
    return totalAmount

def dayOfWeek(date):
    #print(type(date))
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    date_split = str(date).split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])
    #print("Today is {}".format(day))
    dayobj = datetime.date(year,month,day)
    weekDay = dayobj.weekday()
    return weekDays[weekDay]

def competitors(year):
    if(year == 2017):
        return 4
    elif(year == 2018):
        return 6
    else:
        return 10

def numOfEmployeeCalc(day):
    if(day == 'Sunday' or day == 'Saturday' or day == 'Friday'):
        return 7
    else:
        return 5

def dataGenerator():
    date_rng =  pd.date_range(start = '1/1/2017', end = '5/5/2019', freq = 'min')
    dataFrame = pd.DataFrame(data = date_rng, columns = ['Date_Time'], index = date_rng)
    dataFrame = pd.DataFrame(data = dataFrame, index = date_rng).between_time('11:30', '23:30')
    dataFrame['Date of Arrival'] = [d.date() for d in dataFrame['Date_Time']]
    dataFrame['Time of Arrival'] = [d.time() for d in dataFrame['Date_Time']]
    dataFrame['Month'] = pd.to_datetime(dataFrame['Date of Arrival'].astype(str)).dt.month.astype(int)
    dataFrame['Day'] = pd.to_datetime(dataFrame['Date of Arrival'].astype(str)).dt.day.astype(int)
    dataFrame['Day of week'] = dataFrame['Date of Arrival'].map(lambda x : dayOfWeek(x))
    dataFrame['Hour'] = pd.to_datetime(dataFrame['Time of Arrival'].astype(str)).dt.hour.astype(int)
    dataFrame['Week'] = dataFrame['Day'].map(lambda x : int(np.ceil(x/7)))
    dataFrame['Year'] = pd.to_datetime(dataFrame['dateOfArrival'].astype(str)).dt.year.astype(int)
    dataFrame['competitors'] = dataFrame['Year'].map(lambda x : competitors(x))
    #dataFrame['Items_Ordered'] = dataFrame['Time of Arrival'].map(lambda x : rand.sample(population=list(Products_dict.keys()), k=rand.randint(2,8)))
    #dataFrame['Discount(Boolean)'] = dataFrame['Day'].map(lambda x : rand.choice([True, False]))
    #dataFrame['Discount(Boolean)'].where 
    dataFrame['Group of People'] = dataFrame['Time of Arrival'].map(lambda x : rand.randint(1,6))
    dataFrame['Table Number'] = dataFrame['Group of People'].map(lambda x : rand.choice(Table_numbers[x]))
    dataFrame['Items_Ordered'] = dataFrame['Group of People'].apply(lambda x : rand.sample(population=list(Products_dict.keys()), k=rand.randint(x,int(x)+4)))
    dataFrame['Total Amount'] = dataFrame['Items_Ordered'].map(lambda x:price_calculator(x) )
    dataFrame['numOfEmployee'] = dataFrame['dayOfWeek'].map(lambda x : numOfEmployeeCalc(x))
    dataFrame.head(30)
    

    
