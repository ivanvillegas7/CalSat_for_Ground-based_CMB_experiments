# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:59:57 2023

@author: Iván Villegas Pérez

This Python script that imports numpy, matplotlib.pyplot and the List type from
the typing module. The script defines a function called "plot_angles" that takes
no parameters and returns no values.

Within the "plot_angles" function, the script defines several variables,
including the Earth's radius, a conversion factor from degrees to radians, and
arrays for altitude, inclination, and elevation angle. The function then uses a
for loop to calculate the inclination and elevation angle values for each
altitude in the array.

Finally, the function uses matplotlib.pyplot to create two plots: one of
elevation angle vs. altitude, and another of inclination vs. altitude. The plots
are saved to PDF files.
"""

#Import different packages

import numpy as np

from typing import List

import matplotlib.pyplot as plt

def plot_angles():
    
    '''
    This function plots the elevation angle and the inclination against the
    altitude after simulating their values.
    
    Parameters:
        
        none
        
    Returns:
        
        none
    '''
    
    R: float = 6371 #Earth radius in km

    convert: float = np.pi/180 #Converts degrees to radians
    
    h: List[float] = np.linspace(350, 1400, 100000) #Altitude in km

    #Coefficients found in Luis' TFM

    mu: float = 398600.440 #km^3/s^2

    J_2: float = 1.08263e-3

    OmegaDOT: float = 0.9856/(24*60*60) #degrees/s
    
    #Creates list for the inclination

    inclination: List[float] = []
    
    #Creates list for the elevation angle

    el_ang: List[float] = []

    #Creates list for the elevation angle following Luis' method

    el_ang_TFM: List[float] = []

    for i in range(0, len(h)):

        #Adds inclination values in degrees (º)        

        inclination.append(convert**(-1)*(np.arccos(-1*convert*(2*OmegaDOT*\
                                (h[i]+R)**(7/2))/(3*J_2*R**2*np.sqrt(mu)))))

        beta: float = 90-inclination[i] #degrees

        #Adds elevation angle values in degrees (º)

        el_ang.append(-np.arctan(h[i]/(convert*(beta)*R))/convert)

        #Adds Luis' elevation angle values in degrees (º)

        el_ang_TFM.append(-np.arctan((h[i]-(R+h[i])*np.sqrt((beta*convert)**2-\
            np.sin(beta*convert)**2))/((h[i]+R)*np.sin(beta*convert)))/convert)

    #Plots elevation angle against altitude

    plt.figure()

    plt.plot(h, el_ang, color='blue', label='My computation')

    plt.plot(h, el_ang_TFM, color='red', label="Luis' computation")

    plt.xlabel('Altitude [Km]')

    plt.ylabel('Elevation angle [º]')

    plt.title('Elevation angle vs Altitude')

    plt.grid(True)

    plt.legend()

    plt.savefig('../Python Plots/Elevation Angle.pdf')

    #Plots elevation angle against altitude

    plt.figure()

    plt.plot(h, inclination, color='blue')

    plt.xlabel('Altitude [Km]')

    plt.ylabel('Inclination [º]')

    plt.title('Sun-Synchronous Condition')

    plt.grid(True)

    plt.savefig('../Python Plots/SSO.pdf')
