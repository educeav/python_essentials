# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:53:48 2023

@author: edu_c
"""

def isYearLeap(year):
  if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
      return True
  else:
      return False
 

def daysInMonth(year, month):
    meses_31 = [1,3,5,7,8,10,12]
    meses_30 = [4,6,9,11]
    if (month in meses_31):
        return 31 
    elif (month in meses_30):
        return 30
    elif (month == 2):
        if (isYearLeap(year)):
            return 29
        else:
            return 28 
    else:
        return None

def dias_del_anio(year, month, day):
    dias = 0
    if not((month > 0 and month <12) and (year > 0) and (day > 0 and day <= (daysInMonth(year, month)))):
        return None
    for i in range (1, month):
        dias += daysInMonth(year, i)
    dias += day
    return dias



print(dias_del_anio(2023,5,19)) #debe imprimir 139
print(dias_del_anio(2023,2,29)) #debe imprimir none