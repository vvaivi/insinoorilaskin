#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:53:50 2025

@author: konsta

Headloss and pump sizing calculation
"""

# Import libraries
import numpy as np
from matplotlib import pyplot as plt
import friction_factor as ff

# Pump net positive suction head calculations
def calculate_NPSHa(p_s, rho, g, z_water, z_pump, h_L, p_v, NPSHr):
    NPSHa = (p_s)/(rho*g) + (z_water-z_pump) - h_L - p_v/(rho*g)
    if NPSHa > NPSHr:
        print("Pump is safe to operate.")
    else:
        print("Pump is prone to cavitating")
    return NPSHa

# General constants
C2K = 273.15    # Celsius to Kelvin
bar = 100000    # Pa
g = 9.81        # m/s^2
atm = 101325    # Pa


# Hydraulic system properties
z1 = 2          # m
z_water = 0     # m water surface level
z2 = 11         # m
p1 = 1.5 * bar  # Pa
rho = 1000      # kg/m^3
V_1 = 0         # m/s, can be zero if pipe diameter does not change
V_2 = 0         # m/s, can be zero if pipe diameter does not change
K_L = 0         # sum of loss coefficients
m = 1.6         # kg/s
nu = 1.0034e-6  # m2/s
mu = nu*rho     # dynamic viscosity
p_s = 101325    # Pa, pressure at water surface

# Calculate required pump head or system pressure depending on inputs
h_p_input = 0  # m
p2 = 4.14 * bar # bar


# Pipe properties
L = 1160        # m
D_H = 0.053     # m
epsilon= 0.03e-3  # pipe roughness


# Calculated properties
A_c = np.pi*D_H**2/4 # m^2
Q = m/rho       # m^3*s^-1
Re = 4*np.abs(Q)/(nu*np.pi*D_H)
f_D = ff.f_D_WhiteColebrook(D_H, epsilon, Re)

# Dynamic headloss
h_L = (f_D*L/D_H+K_L) * ((Q**2)/(2*g*A_c**2))
print("Dynamic headloss:", h_L, "m")

# Find system pressure or required pump pressure
if h_p_input == 0:
    h_p = (p2-p1 - rho*g*(z1-z2))/(rho*g) + h_L
    print("Required pump head h_p:", h_p, "m")
else:
    p2 = p1 + rho*g*(z1-z2) + rho*g*(h_p_input - h_L)
    print("System head:", p2/bar, "bar")
    


# Static headloss
h_static = z2-z1 + (p2-p1)/(rho*g) + (V_2**2 - V_1**2)/(2*g)
print("Static headloss:", np.round(h_static,2), "m")


# Dynamic headloss
h_dynamic = (f_D*L/D_H+K_L) * ((Q**2)/(2*g*A_c**2))
print("Dynamic headloss:", h_dynamic, "m")

z_pump = z1 # m
#h_L = -0.1 # m
h_L = 0.1   # m, calculated with h_L or entered manually
NPSHr = 3   # m, NPSH required by pump manufacturer
p_v = 2340  # Pa, water partial pressure at calculated temp
NPSHa = calculate_NPSHa(p_s, rho, g, z_water, z_pump, h_L, p_v, NPSHr)
print("NPSHa:", NPSHa)
