import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

cos = np.cos
sin = np.sin
pi = np.pi

def y(x):
    """Function to test"""
    return sqrt(x) + cos(x)
    
def analyticDeriv_y(x):
    """The analytical derivative of sqrt(x) + cos(x)"""
    return 1 / (2 * sqrt(x)) - sin(x))
    
def linearInterpol_y(x, x0, x1):
    min = y(x0)
    slope = (y(x1) - y(x0)) / x1 - x0
    distance = x - x0
    return min + (slope * distance)
    
if __name__ == "__main__":
    
    
