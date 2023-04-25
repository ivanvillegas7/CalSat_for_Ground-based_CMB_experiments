# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:05:01 2023

@author: Iván Villegas Pérez

This Python script provides a simple program for simulating satellite
experiments. The main() function includes different functionalities:

    - Plotting graphs of elevation and inclination angles against altitude.
    - Asking the user to choose between simulating one experiment or all of
      them.
    - If the user chooses to simulate one experiment, the program asks for the
      experiment name, checks if it is among the available experiments and then
      performs two tests: one to count how many times the satellite is seen by
      the experiment, and another to perform a thermal control test.
      
If the user chooses to simulate all experiments, the program checks each
experiment and performs the same two tests for each one.

The code imports the following packages:

    - typing.List: used to define the data type of the experiments list.
    - angles: a module that contains a function to plot graphs of elevation and
      inclination angles against altitude.
    - counts: a module that contains a function to count how many times the
      satellite is seen by a given experiment.
    - thermal_control: a module that contains a function to perform a thermal
      control test for a given experiment.

The experiments list contains the names of four different experiments: QUIJOTE,
CLASS, ACT, and LSPE-STRIP. These experiments are used by the program to check
if the user has entered a valid experiment name.

The program first calls the plot_angles() function to plot the graphs of
elevation and inclination angles against altitude. Then, it asks the user to
choose between simulating one experiment or all of them. If the user chooses to
simulate one experiment, the program asks for the experiment name, checks if it
is among the available experiments, and then performs two tests: one to count
how many times the satellite is seen by the experiment, and another to perform
a thermal control test. If the user chooses to simulate all experiments, the
program checks each experiment and performs the same two tests for each one.
Finally, the program prints a message if the chosen option is not valid.
"""

#Import different packages

from typing import List

import angles

import counts

import thermal_control

#Studied experiments

experiments: List[str] = ['QUIJOTE', 'CLASS', 'ACT', 'LSPE-STRIP']

def main():
    
    """
    It's a simple program that plots graphs of elevation and inclination angles
    against altitude, then asks the user whether they want to simulate one
    experiment or all of them. If the user chooses to simulate one experiment,
    the program asks for the name of the experiment, checks if it is among the
    available experiments, and then performs two tests: one to count how many
    times the satellite is seen by the experiment, and another to perform a
    thermal control test. If the user chooses to simulate all experiments,
    the program checks each experiment and performs the same two tests for each
    one.
    """
    
    #Plots the graphs of the elevation and incliantion angles agaist altitude

    angles.plot_angles()

    print('')

    #Print a message saying the plots are done

    print('Elevation and inclination angles have been plotted.')

    print('')
    
    option: str = input('Do you want to simulate for one experiment (1) or all of them (All)? ')
    
    if option=='1':
        
        print('')

        #Asks for the experiment name

        experiment: str = input('Type your experiment (QUIJOTE, CLASS, ACT or LSPE-STRIP): ')

        print('')

        #Checks if the experiemnt is among the experiments we have data of

        while experiment not in experiments:
            
            #If not, sends a warning message

            print('Try one of the three mentioned experiments (QUIJOTE, CLASS, ACT or LSPE-STRIP).')

            print('')

            #Reasks for the experiemnt name

            experiment: str = input('Type your experiment (QUIJOTE, CLASS, ACT or LSPE-STRIP): ')

            print('')
         
        #Tells how many time the satelline is seen by the studied experiment    

        counts.counts(experiment)
        
        #Does the thermal control test

        thermal_control.thermal_control(experiment)
        
    elif option=='All':
        
        #Checks all the posible studied experimetns at once

        print('')

        for i in range(0, len(experiments)):
            
            #Tells how many time the satelline is seen by the studied experiment    

            counts.counts(experiments[i])
            
            #Does the thermal control test
            
            thermal_control.thermal_control(experiments[i])
            
    else:
        
        print('')
        
        print("That's not an option.")
  
#Run the main code      
  
main()
