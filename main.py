#! /usr/bin/env python3
import parse_temps
import sys
from CpuTemps import cpuTemps
from calculations import calcInterpolation,calcLeastSquare
from output import output

def main():
    try:
        input_temps = sys.argv[1]  # setting command line argument to be input
    except:
        print('You must provide input file of CPU core temps by time step')
        sys.exit(1)
    list = []
    with open(input_temps,'r') as temps_file:
        #Opening the input file provided in the command line argument and calling the parse_temps function from the parse_temps.py file provided by
        # Professor Kennedy to parse and store all of the CPU data in tuples. Than it takes that and stores it in a list that was created above.
        for temps in parse_temps.parse_raw_temps(temps_file):
            list.append(cpuTemps(temps[0],temps[1][0],temps[1][1],temps[1][2],temps[1][3]))
    for x in range(len(list)-1):
        # For loop calling calcInterpolation for 2 objects in the list x and x+1 starting at the first and going to the
        # last object in the list. This calculates the linear interpolation line between the points for each core.
        calcInterpolation(list[x],list[x+1])
    line0,line1,line2,line3, = calcLeastSquare(list)  #Setting line0,line1,line2,line3 equal to the return values of calcLeastSquare() function.

    output(list,line0,line1,line2,line3) #Calling the output() function which writes to each CPU cores respective file with all linear interpolation lines
    # and the single least squares approximation line for each core.

if __name__ == '__main__':
    main()