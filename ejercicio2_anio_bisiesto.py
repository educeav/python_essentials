# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:15:58 2023

@author: edu_c
"""

def es_anio_bisiesto(anio):
    if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        return True
    else:
        return False

#Código provisto
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = es_anio_bisiesto(yr) #cambia el nombre del método
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")