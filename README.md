# Prácticas IFCA
GitHub containing the used codes and plots made for my intership at IFCA.

The main goal of this internship has been to colaborate in the development and characterization of a calibration source boarded in a LEO orbit satellite, in order to calibrate terrestrial experiments of the polarization of the Cosmic Microwave Background (CMB).

The orbit of the calibration satellite (CalSat) can be found at folder 'Orbits' with different durations. In folder 'Code' can be found all the Python scripts used. Running the file 'main.py' will generate all the plot that can be found on folder 'Pyhton Plots' and counts how many times CalSat orbits above (or in the filed of view of) each of the studied experiemnts (QUIJOTE, CLASS, ACT and LSPE-STRIP). You can also find a plot of how the inclination angle changes against altitude for a Sun Synchronus Orbit ('SSO.pdf') and how the elevation angle changes against altitude at the South Pole, where the South Pole Telescope (SPT) is. 

To simulate the orbit of the satellite the software GMAT (General Mission Analysis Tool) has been used, running the file 'CalSat.script'. I could not upload the different generated files with a different starting time due to its weight, however, you have instructions on how to recreate those simulations (just change the starting time in 'CalSat.script') in 'Practicum Report - Iván Villegas Pérez.pdf'.
