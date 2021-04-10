import CpuTemps

def calcLeastSquare(list):
    xsum = sum(t.time for t in list)
    y0sum = sum(c.core0 for c in list)
    y1sum = sum(c.core1 for c in list)
    y2sum = sum(c.core2 for c in list)
    y3sum = sum(c.core3 for c in list)
    xy0sum = sum(xy.time * xy.core0 for xy in list)
    xy1sum = sum(xy.time * xy.core1 for xy in list)
    xy2sum = sum(xy.time * xy.core2 for xy in list)
    xy3sum = sum(xy.time * xy.core3 for xy in list)
    xsqr = sum(x.time*x.time for x in list)
    n = len(list)
    slope0 = (((n * xy0sum) - (xsum * y0sum)) / ((n * xsqr) - (xsum**2)))
    slope1 = (((n * xy1sum) - (xsum * y1sum)) / ((n * xsqr) - (xsum ** 2)))
    slope2 = (((n * xy2sum) - (xsum * y2sum)) / ((n * xsqr) - (xsum ** 2)))
    slope3 = (((n * xy3sum) - (xsum * y3sum)) / ((n * xsqr) - (xsum ** 2)))
    b0 = (((y0sum) - (slope0 * xsum)) / (n))
    b1 = (((y1sum) - (slope1 * xsum)) / (n))
    b2 = (((y2sum) - (slope2 * xsum)) / (n))
    b3 = (((y3sum) - (slope3 * xsum)) / (n))
    y0 = f'{list[0].time:5} <= x < {list[-1].time:5}; y        =   {b0:11.4f}   +   {slope0:8.5f}x; least squares'
    y1 = f'{list[0].time:5} <= x < {list[-1].time:5}; y        =   {b1:11.4f}   +   {slope1:8.5f}x; least squares'
    y2 = f'{list[0].time:5} <= x < {list[-1].time:5}; y        =   {b2:11.4f}   +   {slope2:8.5f}x; least squares'
    y3 = f'{list[0].time:5} <= x < {list[-1].time:5}; y        =   {b3:11.4f}   +   {slope3:8.5f}x; least squares'

    return y0, y1, y2, y3
"""
    Takes a list containing objects of the class cpuTemps. For each object it has the time step and all of the CPU core's temperatures with respect to those time steps.
    Calculates the least squares approximation line for each CPU core across all of the time steps.

    Args:
        list: a list of objects from the cpuTemps class that were parsed in from the input file.

    Yields:
        The least squares approximation line for each core 0,1,2,3 titled y0,y1,y2,y3 respectively.
"""
def calcInterpolation(o1,o2):
    o1.slope0 = ((o2.core0 - o1.core0) / (o2.time - o1.time))
    o1.yIntercept0 = (o1.core0 - ((o2.core0 - o1.core0) / (o2.time - o1.time))*o1.time)
    o1.slope1 = ((o2.core1 - o1.core1) / (o2.time - o1.time))
    o1.yIntercept1 = (o1.core1 - ((o2.core1 - o1.core1) / (o2.time - o1.time)) * o1.time)
    o1.slope2 = ((o2.core2 - o1.core2) / (o2.time - o1.time))
    o1.yIntercept2 = (o1.core2 - ((o2.core2 - o1.core2) / (o2.time - o1.time)) * o1.time)
    o1.slope3 = ((o2.core3 - o1.core3) / (o2.time - o1.time))
    o1.yIntercept3 = (o1.core3 - ((o2.core3 - o1.core3) / (o2.time - o1.time)) * o1.time)
"""
    Takes 2 objects of the cpuTemps class and calculates the slope and y intercept between the two points using the time step as the x value 
    and the CPU core's temperature as the y value. Each core 0,1,2, and 3 have the slope and y-intercept calculated to determine the linear
    interpolation line to the next time step and CPU temperature.

    Args:
        o1: The first object. Contains the time step and the corresponding temperatures for core 0,1,2, and 3 at that time.
        o2: The next object after o1. Again contains the time step and corresponding temperatures for each core at that time.

    Yields:
        slope0,slope1,slope2, and slope3 as well as yIntercept0 through yIntercept4. The linear interpolation line between each point of (time,temp) 
        for each core can now be determined having the slope and y-intercept stored as an attribute for each core for each object in the list.
"""