# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:05:06 2024

@author: Caleb Bowman
"""
import matplotlib.pyplot as plt


crl=open('coloradoriverlevels.txt')

crllines=crl.readlines()

rl=[]
time=[]
date=[]

for i in range(125,221):
    crldata=crllines[i]
    data=crldata.split()
    for index in range(len(data)):
        columns = crldata.split()
        rainfall=columns[5]
        times=columns[3]
        dates=columns[2]
        rl.append(float(rainfall))
        time.append(times)
        date.append(dates)
newtime=[item.replace(':','') for item in time]
plt.plot(time, rl,color='g')
plt.ylabel("Water Level (ft)")
plt.xlabel("Time (CDT)")
plt.xticks(time[::70],rotation=45)
plt.grid(True)
plt.title("Colorado River at Austin, TX October 31,2013")
        
