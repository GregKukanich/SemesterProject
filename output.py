#! /usr/bin/env python3
def output(list,line0,line1,line2,line3):
     f0 = open("interpolation-core-0.txt", "w")
     f0.write(line0 + "\n") #writes the least squares approximation line for all the points for this core
     f1 = open("interpolation-core-1.txt", "w")
     f1.write(line1 + "\n") #writes the least squares approximation line for all the points for this core
     f2 = open("interpolation-core-2.txt", "w")
     f2.write(line2 + "\n") #writes the least squares approximation line for all the points for this core
     f3 = open("interpolation-core-3.txt", "w")
     f3.write(line3 + "\n") #writes the least squares approximation line for all the points for this core
     for ctr in range(len(list)-1):
     #This for loop writes all of the linear interpolation lines between each time step and core temp to each cores respective file
        f0.write(f'{list[ctr].time:5} <= x < {list[ctr+1].time:5}; y_{ctr:<4}   =   {list[ctr].yIntercept0:>11.4f}   +   {list[ctr].slope0:>8.4f}x; interpolation \n')
        f1.write(f'{list[ctr].time:5} <= x < {list[ctr+1].time:5}; y_{ctr:<4}   =   {list[ctr].yIntercept1:>11.4f}   +   {list[ctr].slope1:>8.4f}x; interpolation \n')
        f2.write(f'{list[ctr].time:5} <= x < {list[ctr+1].time:5}; y_{ctr:<4}   =   {list[ctr].yIntercept2:>11.4f}   +   {list[ctr].slope2:>8.4f}x; interpolation \n')
        f3.write(f'{list[ctr].time:5} <= x < {list[ctr+1].time:5}; y_{ctr:<4}   =   {list[ctr].yIntercept3:>11.4f}   +   {list[ctr].slope3:>8.4f}x; interpolation \n')
"""
    Takes a list containing objects of the class cpuTemps. For each object it has the time step and all of the CPU core's temperatures with respect to those time steps.
    Calculates the least squares approximation line for each CPU core across all of the time steps.

    Args:
        list: a list of objects from the cpuTemps class that were parsed in from the input file. Contains the time steps and corresponding core temperatures
        as well as the now calculated slope and y-intercept between each point for the linear interpolation equations.
        line0: The least squares approximation line for core0.
        line1: The least squares approximation line for core1.
        line2: The least squares approximation line for core2.
        line3: The least squares approximation line for core3.
        

    Yields:
        Outputs to 4 files corresponding to each core titled "interpolation-core-x.txt". Containing the all of the linear interpolation lines calcualted
        as well as the single least squares approximation line.
"""