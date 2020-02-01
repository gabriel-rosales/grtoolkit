import math

def a_rad(v_rad,R):
    """
    Usage: acceleration for uniform circular motion

    Variables: 
        v_rad=radial velocity
        R = radius"""
    return v_rad**2/R

def v_rad(R,T):
    """
    Usage: velocity for uniform circular motion

    Variables: 
        T = period
        R = radius"""
    return 2*math.pi*R/T