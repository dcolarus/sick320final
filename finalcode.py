"""
Final Project ASTR320
Lane Emden Equation (LEE) and Specific Solutions
Authors: Emma Kleiner, Dan Bordwin, Dominic Colarusso
13 May 2021

This code is adapted from TheoreticalAstrophysicsCPH YouTube channel (2019)
"""

Still needs improvements

import seaborn as sns
import matplotlib.pyplot as plt

#Set color scheme
sns.set_palette("magma",8)

############# Use trapezoidal integration technique
## This technique will give us a quick understanding of some of the 
#### solutions without creating much of a computational challenge

dxi = 0.001  #bin size for integration, xi is the dimensionless variable in LEE
N = 10000    #no. bins

for n in range(8):
    #initial values
    xi = 0.01
    theta = 1.0 #function of f1 and xi
    f1 = 0.0   #function of xi and theta
    
    theta_sol = []
    xi_sol = []
    
    for i in range(N):
        
        f1 += -xi**2 * theta**(n) * dxi   #integrate f1
        theta += f1/xi**2 * dxi       #integrate theta
        xi += dxi
        
        theta_sol.append(theta)   #add new solutions
        xi_sol.append(xi)         #add new solutions
    #Print the intersections with y = 0    
        if (theta_sol[i]<0 and theta_sol[i-1]>=0):
            print(n,xi)
        if (theta_sol[i]>0 and theta_sol[i-1]<=0):
            print(n,xi)
    plt.plot(xi_sol,theta_sol)
    
plt.xlim(0,10)
plt.ylim(-0.4,1)
plt.xlabel(r'$\xi$')
plt.ylabel(r'$\theta$')
plt.title('Solutions for the Lane-Emden Equation for n = [0,7]')
plt.hlines(0,0,10,'gray','dashed')
plt.show()