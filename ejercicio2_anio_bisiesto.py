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

anio = int(input("Ingrese un año "))
print(es_anio_bisiesto(anio))

