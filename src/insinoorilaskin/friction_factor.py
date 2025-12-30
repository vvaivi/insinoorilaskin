#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 13:55:16 2025

@author: konsta
"""
import numpy as np
from scipy import optimize

def f_D_WhiteColebrook(D_H: float, epsilon: float, Re: float) -> float:
    if Re < float(2300):
        f_D = 64 / Re
    elif Re <= 4000:
        f_D = (64/Re + 0.25*(np.log10((epsilon/D_H)/3.7 + 5.74/Re**0.9))**-2)/2
    else:
        print("Turbulentti virtaus")
        def colebrook(f, Re, epsilon, D_H):
            
            return 1/np.sqrt(f) + 2*np.log10(
                epsilon/(3.7*D_H) + 2.51/(Re*np.sqrt(f)))
        
        result = optimize.root_scalar(
            colebrook,
            args=(Re, epsilon, D_H),
            bracket=[1e-6, 0.2],
            method='brentq')
        
        f_D = result.root
        print("Kitkakerroin:", f_D)
    return f_D