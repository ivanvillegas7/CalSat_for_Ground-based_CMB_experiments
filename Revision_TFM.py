# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:04:05 2021

@author: Iván
"""

#Import different packages

import numpy as np

from typing import List

import matplotlib.pyplot as plt

#Define all the different functions

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

    plt.savefig('Elevation Angle.pdf')

    #Plots elevation angle against altitude

    plt.figure()

    plt.plot(h, inclination, color='blue')

    plt.xlabel('Altitude [Km]')

    plt.ylabel('Inclination [º]')

    plt.title('Sun-Synchronous Condition')

    plt.grid(True)

    plt.savefig('SSO.pdf')

def time_convert(seconds: float) -> str:
    
    '''
    This function converts the total time in seconds to days, hours, minutes
    and seconds for a better presentation.
    
    Parameters:
        
        none
        
    Returns:
        
        none
    '''

    #Computes the complete number of days

    days: int = seconds // (24*60*60)

    #Computes the complete number of remaining seconds

    seconds: int = seconds % (24*60*60)

    #Checks if it can only be expressed as days

    if seconds == 0:

        return(f'{int(days)} days')

    else:
        
        #Computes the complete number of remaining hours

        hours: int = seconds // (60*60)

        #Computes the complete number of remaining seconds

        seconds: int = seconds % (60*60)

        #Checks if it can only be expressed as days and hours

        if seconds == 0:

            return(f'{int(days)} days, {int(hours)} hours')

        else:

            #Computes the complete number of remaining minutes            

            minutes: int = seconds // (60)
            
            #Computes the complete number of remaining seconds
            
            seconds: int = seconds % (60)
            
            #Checks if it can only be expressed as days, hours and minutes
            
            if seconds == 0:

                return(f'{int(days)} days, {int(hours)} hours, {int(minutes)} minutes')

            else:

                return(f'{int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds')

def counts(experiment: str):
    
    '''
    This functions prints how many time the studied experiemnt has stablish
    contact (has seen) the calibration satellite (CalSat) in a certain time
    determined during the simulation usig the GMat software.
    
    Parameters:
        
        experiment: name of the studied experiment
        
    Returns:
        
        none
    '''
    
    #Initialises the time use to check if it is a different orbit to 0 s
    
    saved_time: float = 0

    count: int = 0 #Initialises the count of contacts to 0
      
    #Starts plotting the data
    
    plt.figure()
    
    plt.xlabel('Longitude [º]')
    
    plt.ylabel('Latitude [º]')
    
    plt.title(f'{experiment}')
    
    #Check which experiment is going to be studied

    if experiment == experiments[0]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        angular_position: List[float] = [28.300016667, -16.506]

        angular_aperture: float = 8 #Angular aperture in degrees(º)

    elif experiment == experiments[1]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        angular_position: List[float] = [-22.966666666, -67.783333333]
     
        angular_aperture: float = 16 #Angular aperture in degrees(º)
        
    elif experiment == experiments[2]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        angular_position: List[float] = [-22.95861111, -67.7875]
     
        angular_aperture: float = 1 #Angular aperture in degrees(º)
        
    elif experiment == experiments[3]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        angular_position: List[float] = [28.30111111, -16.51055556]
     
        angular_aperture: float = 5 #Angular aperture in degrees(º)
    
    if experiment == experiments[1]:
    
        x: List[float] = np.linspace(angular_position[1]-angular_aperture/2,\
                                     angular_position[1]+angular_aperture/2,\
                                     1000)
        
        y1: List[float] = []
        
        y2: List[float] = []
        
        for j in range(0, len(x)):
            
            root: float = np.sqrt((angular_aperture/2)**2-\
                                  (x[j]-angular_position[1])**2)
            
            y1.append(root+angular_position[0])
            
            y2.append(-root+angular_position[0])
        
        plt.plot(x, y1, color='black', label=f'Angular aperture for {experiment}')
        
        plt.plot(x, y2, color='black')
        
    else:
        
        plt.vlines(angular_position[1]-angular_aperture/2,angular_position[0]-angular_aperture/2, angular_position[0]+angular_aperture/2, color='black', label=f'Angular aperture for {experiment}')
            
        plt.vlines(angular_position[1]+angular_aperture/2, angular_position[0]-angular_aperture/2, angular_position[0]+angular_aperture/2, color='black')
            
        plt.hlines(angular_position[0]-angular_aperture/2, angular_position[1]-angular_aperture/2, angular_position[1]+angular_aperture/2, color='black')
            
        plt.hlines(angular_position[0]+angular_aperture/2, angular_position[1]-angular_aperture/2, angular_position[1]+angular_aperture/2, color='black')
    
    #plt.legend()
    
    #Data are imported

    i: int = 0
    
    #Checks for the file; change the route for a different computer
    
    file: str = "../../../../../Otros/Programas/GMat/bin/ReportFile1.txt"

    with  open(file, "r") as infile:

        lines = infile.readlines()

        theta: List[float] = [] #Creates longitud list

        phi: List[float] = [] #Creates latitude list

        time: List[float] = [0] #Creates time list

        for  line in  lines:

            #First row is skipped

            if i==0:

                i+=1

            else:

                vals = line.split()

                theta.append(float(vals[0])) #Adds latitude values

                phi.append(float(vals[1])) #Adds longitude values
                
                long: List[float] = [] #Creates longitud list for plotting
                
                lat: List[float] = [] #Creates latitude list for plotting

                if i==1:

                    t_0: float = float(vals[3]) #Saves initial time

                    i+=1

                else:
                    
                    #Adds time in seconds (s)

                    time.append((float(vals[3])-t_0)*24*60**2)
                    
    for i in range(0, len(time)):
                
        #Checks if the experiment can see CalSat
        
        if experiment==experiments[1]:
            
            if (angular_position[0]-theta[i])**2+\
                (angular_position[1]-phi[i])**2 <=\
                (angular_aperture/2)**2:
                    
                long.append(phi[i]) #Adds longitude values for plotting
                
                lat.append(theta[i]) #Adds latitude values for plotting
                
                #Checks if there is a first contact in the first orbit
    
                if time[i]-saved_time<5544:
                    
                    if count==0:
                    
                        count+=1 #Adds a count to the counter
                        
                        saved_time = time[i] #New reference time
                        
                
    
                #Checks that the contact is in a different orbit (s)
    
                else:
    
                    saved_time = time[i] #New reference time
    
                    count+=1 #Adds a count to the counter
            
            else:
                
                if len(lat)>0:
                
                    plt.plot(long, lat, marker='o', ls='solid')
                
                    lat = []
                    
                    long = []
                    
        else:
            
            if (angular_position[0]-theta[i])**2 <=\
               (angular_aperture/2)**2:
                   
                if (angular_position[1]-phi[i])**2 <=\
                   (angular_aperture/2)**2:
    
                    long.append(phi[i]) #Adds longitude values for plotting
                    
                    lat.append(theta[i]) #Adds latitude values for plotting
                    
                    #Checks if there is a first contact in the first orbit
    
                    if time[i]-saved_time<5544:
                        
                        if count==0:
                        
                            count+=1 #Adds a count to the counter
                            
                            saved_time = time[i] #New reference time
                            
                    
    
                    #Checks that the contact is in a different orbit (s)
    
                    else:
    
                        saved_time = time[i] #New reference time
    
                        count+=1 #Adds a count to the counter
                
            else:
                
                plt.plot(long, lat, marker='o', ls='solid')
            
                lat = []
                
                long = []
                
    time_max: float = time[-1] #Maximum time of the simulation in seconds
                        
    
    #Prints total number of times the studied experiment has made contact
    #with CalSat

    if count==0:

        print(f'CalSat does not pass (0 times) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==1:

        print(f'CalSat passes once (1) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==2:

        print(f'CalSat passes twice (2) over {experiment} experimet in {time_convert(time_max)}.')

    else:

        print(f'CalSat passes {count} times over {experiment} experimet in {time_convert(time_max)}.')

#%%

#Plots the graphs of the elevation and incliantion angles agaist altitude

plot_angles()

print('')

#Print a message saying the plots are done

print('Elevation and inclination angles have been plotted.')

print('')

#%%

#Studied experiments

experiments: List[str] = ['QUIJOTE', 'CLASS', 'ACT', 'LSPE-STRIP'] 

#Uncomment for checking each individual experiment individually

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

counts(experiment)

#%%

#Checks all the posible studied experimetns at once

print('')

for i in range(0, len(experiments)):
    
    counts(experiments[i])
    
    print('')
