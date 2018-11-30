import numpy as np
import math

def GredientDescent(x, y, step_size, tolerance):
    x = np.array(x)
    y = np.array(y)
    pred = np.array([0.0]* len(x))
    slope = 0
    intercept = 0
    magn = 0.05
    j = 0
    while magn > tolerance:
        j += 1
        error = pred - y
        errorSum = np.sum(error)
        intercept = round(intercept - (step_size * errorSum),4)
        slopeSum = np.sum(x * error)
        slope = round(slope - (step_size * slopeSum), 4)
        for i in range(len(x)):
            pred[i] = (slope * x[i]) + intercept
        
        magn = round(math.sqrt(errorSum**2 + slopeSum**2),5)
        print ('Iteration Number: {0}'.format(j))
        print ('Slope: {0} Intercept: {1}'.format(slope,intercept))
    return round(slope,4), round(intercept,4)
