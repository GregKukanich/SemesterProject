#! /usr/bin/env python3
class cpuTemps:
    def __init__(self,time,core0,core1,core2,core3):
        # time is the value of the current time step
        # core0-core4 are the temperatures of each core at the current time step
        #slope0-slope4 are the slopes between each set of points for each CPU core respectively (ie. slope0 is the slope
            # between the current (time,core0) and the next time step values (time,core0))
        #yIntercept0-yIntercept4 are the yintercept values between each set of points for each CPU core respectively similar
            # to slope
        self.time = time
        self.core0 = core0
        self.slope0 = None
        self.yIntercept0 = None
        self.core1 = core1  #Temp
        self.slope1 = None
        self.yIntercept1 = None
        self.core2 = core2
        self.slope2 = None
        self.yIntercept2 = None
        self.core3 = core3
        self.slope3 = None
        self.yIntercept3 = None

