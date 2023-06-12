# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:02:00 2023

@author: Iván Villegas Pérez

The script then defines a list called experiments that contains the names of
four different experiments.

The script then defines a function called counts that takes one parameter
experiment. This function calculates the number of times that a calibration
satellite (CalSat) was seen during the simulation using the GMat software for a
certain amount of time. The function also creates a plot of the data.

Inside the function, the time variable saved_time is initialized to 0 seconds 
and the count variable count is initialized to 0. The script then checks which
experiment is being studied by comparing the parameter experiment to the list
experiments. Depending on which experiment is being studied, the function sets
ang_pos and angular_aperture to different values.

The script then opens a file named "ReportFile.txt" and reads its contents.
The script loops through each line in the file and skips the first line. Then,
the script adds the longitude and latitude values to the theta and phi lists,
respectively. The script also adds the time values to the time list.

The script then creates an empty list long and lat to be used for plotting later.
It loops through the time list, checks if the experiment can see the CalSat
based on its location, and adds the corresponding longitude and latitude values
to long and lat. The script then checks whether the time difference between the
current time and the previously saved time is less than a certain value (5544
seconds, equivalent to one orbit). If it is, and if count is zero, the script
increments count and updates saved_time. If the time difference is greater than
the specified value, the script updates saved_time and increments count.

If lat is not empty, the script plots the corresponding longitude and latitude
values. Finally, the script sets time_max to the last value in the time list.
"""

#Import different packages

import numpy as np

from typing import List

import matplotlib.pyplot as plt

from matplotlib.patches import RegularPolygon

#Studied experiments

experiments: List[str] = ['QUIJOTE', 'CLASS', 'ACT', 'LSPE-STRIP', 'POLARBEAR2']

def counts(experiment: str):
    
    '''
    This functions prints how many time the studied experiemnt has stablish
    contact (has seen) the calibration satellite (CalSat) in a certain time
    determined during the simulation usig the GMat software.
    
    Parameters:
    - experiment (str): name of the studied experiment
        
    Returns:
        
        None
    '''
    
    #Initialises the time use to check if it is a different orbit to 0 s
    
    saved_time: float = 0

    count: int = 0 #Initialises the count of contacts to 0
    
    time_: List[float] = []
      
    #Starts plotting the data
    
    plt.figure()
    
    plt.xlabel('Longitude [º]')
    
    plt.ylabel('Latitude [º]')
    
    plt.title(f'{experiment}')
    
    #Check which experiment is going to be studied

    if experiment == experiments[0]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [28.300016667, -16.506]

        angular_aperture: float = 8 #Angular aperture in degrees(º)

    elif experiment == experiments[1]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.966666666, -67.783333333]
     
        angular_aperture: float = 16 #Angular aperture in degrees(º)
        
    elif experiment == experiments[2]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.95861111, -67.7875]#-28
     
        angular_aperture: float = 1 #Angular aperture in degrees(º)
        
    elif experiment == experiments[3]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [28.30111111, -16.51055556]
     
        angular_aperture: float = 5 #Angular aperture in degrees(º)
        
    elif experiment == experiments[4]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.95805556, -67.7861]
     
        angular_aperture: float = 4.8 #Angular aperture in degrees(º)
    
    x: List[float] = np.linspace(ang_pos[1]-angular_aperture/2,\
                                 ang_pos[1]+angular_aperture/2,\
                                 1000)
    
    y1: List[float] = []
    
    y2: List[float] = []
    
    for j in range(0, len(x)):
        
        root: float = np.sqrt((angular_aperture/2)**2-\
                              (x[j]-ang_pos[1])**2)
        
        y1.append(root+ang_pos[0])
        
        y2.append(-root+ang_pos[0])
    
    plt.plot(x, y1, color='black', label=f'Angular aperture for {experiment}')
    
    plt.plot(x, y2, color='black')
    
    #Data are imported

    i: int = 0
    
    #Checks for the file; change the route for a different computer
    
    file: str = "../../../../../../Programas/GMAT/bin/ReportFile.txt"

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
                
                time_pass: List[float] = []

                if i==1:

                    t_0: float = float(vals[3]) #Saves initial time

                    i+=1

                else:
                    
                    #Adds time in seconds (s)

                    time.append((float(vals[3])-t_0)*24*60**2)
                    
    for i in range(0, len(time)):
                
        #Checks if the experiment can see CalSa
            
        if (ang_pos[0]-theta[i])**2+\
            (ang_pos[1]-phi[i])**2 <=\
            (angular_aperture/2)**2:
                
            long.append(phi[i]) #Adds longitude values for plotting
            
            lat.append(theta[i]) #Adds latitude values for plotting
            
            if len(time_pass)<1:
            
                t_0_: float = time[i]
                
                time_pass.append(0)
                
            else:
                
                time_pass.append(time[i]-t_0_)
            
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
            
                plt.plot(long, lat, marker='.')
                
                time_.append(time_pass[-1])
            
                lat = []
                
                long = []
                
                time_pass = []
                
    time_max: float = time[-1] #Maximum time of the simulation in seconds
    
    #Prints total number of times the studied experiment has made contact
    #with CalSat

    if count==0:

        print(f'\nCalSat does not pass (0 times) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==1:

        print(f'\nCalSat passes once (1) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==2:

        print(f'\nCalSat passes twice (2) over {experiment} experimet in {time_convert(time_max)}.')

    else:

        print(f'\nCalSat passes {count} times over {experiment} experimet in {time_convert(time_max)}.')

    plt.savefig(f'../Python Plots/{experiment}/{experiment}.jpg')
    
    print(f'\n Minimum duration: {np.min(np.array(time_))}s.')
    
    print(f'\n Maximum duration: {np.max(np.array(time_))}s.')
    
    print(f'\n Mean duration: {np.mean(np.array(time_))}s.')
    
    print(f'\n Total duration: {np.sum(np.array(time_))}s.')
    
def time_convert(seconds: float) -> str:
    
    '''
    This function converts the total time in seconds to days, hours, minutes
    and seconds for a better presentation.
    
    Parameters:
    - seconds (float): the number of seconds that have been simulated in GMAT
        
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

def inside_hexagon(center: float, long: float, lat: float, l):
    
    h: List[float] = [0, 1]
    
    s1: List[float] = [np.sqrt(3)/2, 1/2]
    
    s2: List[float] = [np.sqrt(3)/2, -1/2]
    
    V: List[float] = [long-center[0], lat-center[1]]
    
    if V[0]*h[0]+V[1]*h[1]<=l**2:
        
        if V[0]*s1[0]+V[1]*s1[1]<=l**2:
            
            if V[0]*s2[0]+V[1]*s2[1]<=l**2:
                
                return True
            
    else:
        
        return False
    
def condition(centers: List[List[float]], long: float, lat: float, l: float):
    
    opt: bool = False
    
    for c in centers:
        
        if opt==False:
        
            opt = inside_hexagon(c, long, lat, l)
            
        elif opt==True:
            
            break
        
    return opt

def counts_hex(experiment):
    
    '''
    This functions prints how many time the studied experiemnt has stablish
    contact (has seen) the calibration satellite (CalSat) in a certain time
    determined during the simulation usig the GMat software.
    
    Parameters:
    - experiment (str): name of the studied experiment
        
    Returns:
        
        None
    '''
    
    #Initialises the time use to check if it is a different orbit to 0 s
    
    saved_time: float = 0

    count: int = 0 #Initialises the count of contacts to 0
    
    time_: List[float] = []
      
    #Starts plotting the data
    
    fig, ax = plt.subplots(1)
    
    ax.set_xlabel('Longitude [º]')
    
    ax.set_ylabel('Latitude [º]')
    
    ax.set_title(f'{experiment}')
           
    #Check which experiment is going to be studied

    if experiment == experiments[0]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [28.300016667, -16.506]

        angular_aperture: float = 8 #Angular aperture in degrees(º)

    elif experiment == experiments[1]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.966666666, -67.783333333]
     
        angular_aperture: float = 16 #Angular aperture in degrees(º)
        
    elif experiment == experiments[2]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.95861111, -67.7875]#-28
     
        angular_aperture: float = 1 #Angular aperture in degrees(º)
        
    elif experiment == experiments[3]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [28.30111111, -16.51055556]
     
        angular_aperture: float = 5 #Angular aperture in degrees(º)
        
    elif experiment == experiments[4]:
        
        #Latitude and longitude in degrees (North-South, East-West)

        ang_pos: List[float] = [-22.95805556, -67.7861]
     
        angular_aperture: float = 4.8 #Angular aperture in degrees(º)
    
    x: List[float] = np.linspace(ang_pos[1]-angular_aperture/2,\
                                 ang_pos[1]+angular_aperture/2,\
                                 1000)
    
    y1: List[float] = []
    
    y2: List[float] = []
    
    for j in range(0, len(x)):
        
        root: float = np.sqrt((angular_aperture/2)**2-\
                              (x[j]-ang_pos[1])**2)
        
        y1.append(root+ang_pos[0])
        
        y2.append(-root+ang_pos[0])
    
    plt.plot(x, y1, color='black', label=f'Angular aperture for {experiment}')
    
    plt.plot(x, y2, color='black')
    
    l: float = np.sqrt(7)*angular_aperture/14 #Side of the hexagon in degrees(º)
    
    offCoord = [[ang_pos[1], ang_pos[0]],\
                [ang_pos[1]+3*l/2, ang_pos[0]-np.sqrt(3)*l/2],\
                [ang_pos[1], ang_pos[0]-np.sqrt(3)*l],\
                [ang_pos[1]-3*l/2, ang_pos[0]+np.sqrt(3)*l/2],\
                [ang_pos[1], ang_pos[0]+np.sqrt(3)*l],\
                [ang_pos[1]+3*l/2, ang_pos[0]+np.sqrt(3)*l/2],\
                [ang_pos[1]-3*l/2, ang_pos[0]-np.sqrt(3)*l/2]]

    ax.set_aspect('equal')

    for c in offCoord:
        # fix radius here
        hexagon = RegularPolygon((c[0], c[1]), numVertices=6, radius=l,\
                                 orientation=np.pi/2, ec='black', fc='none')
        ax.add_patch(hexagon)
    plt.autoscale(enable = True)
    
    #Data are imported

    i: int = 0
    
    #Checks for the file; change the route for a different computer
    
    file: str = "../../../../../../Programas/GMAT/bin/ReportFile.txt"

    with  open(file, "r") as infile:

        lines = infile.readlines()

        th: List[float] = [] #Creates longitud list

        phi: List[float] = [] #Creates latitude list

        time: List[float] = [0] #Creates time list

        for  line in  lines:

            #First row is skipped

            if i==0:

                i+=1

            else:

                vals = line.split()

                th.append(float(vals[0])) #Adds latitude values

                phi.append(float(vals[1])) #Adds longitude values
                
                long: List[float] = [] #Creates longitud list for plotting
                
                lat: List[float] = [] #Creates latitude list for plotting
                
                time_pass: List[float] = []

                if i==1:

                    t_0: float = float(vals[3]) #Saves initial time

                    i+=1

                else:
                    
                    #Adds time in seconds (s)

                    time.append((float(vals[3])-t_0)*24*60**2)
                    
    for i in range(0, len(time)):
                
        #Checks if the experiment can see CalSat
        """    
        if th[i]<=ang_pos[0]+np.sqrt(3)*l and th[i]>=ang_pos[0]-np.sqrt(3)*l:
               
            if phi[i]<=ang_pos[1]+2*l and phi[i]>=ang_pos[1]-2*l:
                
                long.append(phi[i]) #Adds longitude values for plotting
                
                lat.append(th[i]) #Adds latitude values for plotting
                
                if len(time_pass)<1:
                
                    t_0_: float = time[i]
                    
                    time_pass.append(0)
                    
                else:
                    
                    time_pass.append(time[i]-t_0_)
                
                #Checks if there is a first contact in the first orbit
    
                if time[i]-saved_time<5544:
                    
                    if count==0:
                    
                        count+=1 #Adds a count to the counter
                        
                        saved_time = time[i] #New reference time
    
                #Checks that the contact is in a different orbit (s)
    
                else:
    
                    saved_time = time[i] #New reference time
    
                    count+=1 #Adds a count to the counter
        
        elif th[i]<=ang_pos[0]+3*np.sqrt(3)*l/2 and th[i]>=ang_pos[0]+np.sqrt(3)*l:
            
            if phi[i]<=ang_pos[1]+l/2 and phi[i]>=ang_pos[1]+l/2:
                
                long.append(phi[i]) #Adds longitude values for plotting
                
                lat.append(th[i]) #Adds latitude values for plotting
                
                if len(time_pass)<1:
                
                    t_0_: float = time[i]
                    
                    time_pass.append(0)
                    
                else:
                    
                    time_pass.append(time[i]-t_0_)
                
                #Checks if there is a first contact in the first orbit
    
                if time[i]-saved_time<5544:
                    
                    if count==0:
                    
                        count+=1 #Adds a count to the counter
                        
                        saved_time = time[i] #New reference time
    
                #Checks that the contact is in a different orbit (s)
    
                else:
    
                    saved_time = time[i] #New reference time
    
                    count+=1 #Adds a count to the counter
        
        elif th[i]<=ang_pos[0]-np.sqrt(3)*l and th[i]>=ang_pos[0]-3*np.sqrt(3)*l/2:
            
            if phi[i]<=ang_pos[1]+l/2 and phi[i]>=ang_pos[1]+l/2:
                
                long.append(phi[i]) #Adds longitude values for plotting
                
                lat.append(th[i]) #Adds latitude values for plotting
                
                if len(time_pass)<1:
                
                    t_0_: float = time[i]
                    
                    time_pass.append(0)
                    
                else:
                    
                    time_pass.append(time[i]-t_0_)
                
                #Checks if there is a first contact in the first orbit
    
                if time[i]-saved_time<5544:
                    
                    if count==0:
                    
                        count+=1 #Adds a count to the counter
                        
                        saved_time = time[i] #New reference time
    
                #Checks that the contact is in a different orbit (s)
    
                else:
    
                    saved_time = time[i] #New reference time
    
                    count+=1 #Adds a count to the counter
                    
        elif th[i]<=ang_pos[0]+5*l/2 and th[i]>=ang_pos[0]+2*l:
            
            if phi[i]<=np.sqrt(3)*(th[i]-1) and phi[i]>=-np.sqrt(3)*(th[i]-1):
                
                long.append(phi[i]) #Adds longitude values for plotting
                
                lat.append(th[i]) #Adds latitude values for plotting
                
                if len(time_pass)<1:
                
                    t_0_: float = time[i]
                    
                    time_pass.append(0)
                    
                else:
                    
                    time_pass.append(time[i]-t_0_)
                
                #Checks if there is a first contact in the first orbit
    
                if time[i]-saved_time<5544:
                    
                    if count==0:
                    
                        count+=1 #Adds a count to the counter
                        
                        saved_time = time[i] #New reference time
    
                #Checks that the contact is in a different orbit (s)
    
                else:
    
                    saved_time = time[i] #New reference time
    
                    count+=1 #Adds a count to the counter
        """
        if condition(offCoord, phi[i], th[i], l)==True:
            
            long.append(phi[i]) #Adds longitude values for plotting
            
            lat.append(th[i]) #Adds latitude values for plotting
            
            if len(time_pass)<1:
            
                t_0_: float = time[i]
                
                time_pass.append(0)
                
            else:
                
                time_pass.append(time[i]-t_0_)
            
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
            
                plt.plot(long, lat, marker='.')
                
                time_.append(time_pass[-1])
            
                lat = []
                
                long = []
                
                time_pass = []
                
    time_max: float = time[-1] #Maximum time of the simulation in seconds
    
    #Prints total number of times the studied experiment has made contact
    #with CalSat

    if count==0:

        print(f'\nCalSat does not pass (0 times) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==1:

        print(f'\nCalSat passes once (1) over {experiment} experimet in {time_convert(time_max)}.')

    elif count==2:

        print(f'\nCalSat passes twice (2) over {experiment} experimet in {time_convert(time_max)}.')

    else:

        print(f'\nCalSat passes {count} times over {experiment} experimet in {time_convert(time_max)}.')

    plt.savefig(f'../Python Plots/{experiment}/{experiment} hexagons.jpg')
    
    print(f'\n Minimum duration: {np.min(np.array(time_))}s.')
    
    print(f'\n Maximum duration: {np.max(np.array(time_))}s.')
    
    print(f'\n Mean duration: {np.mean(np.array(time_))}s.')
    
    print(f'\n Total duration: {np.sum(np.array(time_))}s.')
    
counts_hex('POLARBEAR2')