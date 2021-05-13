"""
Final Project ASTR320
Lane Emden Equation and Specific Solutions
Authors: Emma Kleiner, Dan Bordwin, Dominic Colarusso
13 May 2021

This code is adapted from Nerd_Awesome_YouTuber123 (2043)
"""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_palette("magma",8)

dxi = 0.01
N = 1000

for n in range(8):
    xi = 0.01
    theta = 1.0
    fl = 0.0
    theta_sol = []
    xi_sol = []
    
    for i in range(N):
        
        fl += -xi**2 * theta**(n) * dxi
        theta += fl/xi**2 * dxi
        xi += dxi
        
        theta_sol.append(theta)
        xi_sol.append(xi)

    plt.plot(xi_sol,theta_sol)
    
plt.xlim(0,10)
plt.ylim(-1,1)
plt.show()