#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 15:12:30 2025

@author: facu
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig
import sympy as sp
#%% 
#Simbolos
ZA = sp.symbols('Za', real = True, positive = True)
ZB = sp.symbols('Zb', real = True, positive = True)
R = sp.symbols('R', real = True, positive = True)
#%%
y1 = sp.Matrix ([
    [(R+ZB)/(R*R+R*2*R*ZB), -(ZB)/(R*R+R*2*R*ZB)],
    [-(ZB)/(R*R+R*2*R*ZB), (R+ZB)/(R*R+R*2*R*ZB)]
    ])

y2 = sp.Matrix ([
    [1/ZA, -1/ZA],
    [-1/ZA, (ZA+R)/(ZA*R)]
    ])

yt = y1*y2

yt_fx = yt.subs({R:1, ZA:1, ZB:1})

yt_fx