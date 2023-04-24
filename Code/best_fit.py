# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:05:01 2023

@author: Iván Villegas Pérez

The script defines a function named best_fit that reads data from a file named
antennas.txt, fits a curve to the data using a function of the form a/x+b, where
a and b are constants, plots the data and the best fit, and returns the value of
the fitted function at a given frequency.

The curve_fit function from the scipy.optimize module is used to fit the curve
and the numpy and matplotlib.pyplot modules are imported to handle the data and
plot the results.

It is assumed that the file antennas.txt has two columns separated by whitespace,
where the first column contains the frequency values and the second column
contains the corresponding antenna diameter values. The code also assumes that
the file is located in a directory one level above the directory where the
script is executed, and that a directory named Python Plots exists in the same
directory as the script, where the plots will be saved.

The function func calculates the value of a/x+b given a value of x, a, and b.
The function best_fit takes as input a frequency value f, and returns the value
of the fitted function at that frequency.
"""

#Import different packages

import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

#Function to be fitted
def func(x, a, b):
    """
    This function calculates the value of a/x + b.
    
    Parameters:
    - x (float): The value of the variable x
    - a (float): The value of the parameter a
    - b (float): The value of the parameter b
    
    Returns:
    - f (float): the value of a/x + b
    """
    
    f: float = a/x + b
    
    return f


def best_fit(f: float):
    
    """
    Given a frequency f, this function reads a dataset from a file and performs
    a best fit of the data using a function of the form a/x+b, where a and b are
    constants. It then returns the value of the function for the given frequency.

    Parameters:
    - f (float): The frequency value for which the function is evaluated.

    Returns:
    - value (float): The value of the fitted function at the given frequency.
    """

    data = np.loadtxt('../antennas.txt', skiprows=1)
    
    frequency: np.array(float) = data[:, 0]
    
    diameter = data[:, 1]
    
    #Fits the curve
    popt, pcov = curve_fit(func, frequency, diameter)
    
    a = popt[0]
    b = popt[1]
    
    freq: np.array(float) = np.linspace(10, 240)
    
    #Plots the data and the best fit
    plt.figure()
    plt.plot(frequency, diameter, 'o', label='Data')
    plt.plot(freq, func(freq, *popt), label=f'Fitted curve: y={a:.2f}/x+{b:.2f}')
    plt.plot([f], [a/f+b], 'o', label='Wanted data')
    plt.xlabel(r'Frequency [GHz]')
    plt.ylabel(r'Antenna diameter [m]')
    plt.title('Antenna diameter as a function of frequency')
    plt.grid(True)
    plt.legend()
    plt.savefig(f'../Python Plots/Antenna vs Frequency {f}GHz.pdf')
    
    value: float = func(f, a, b)

    return value
