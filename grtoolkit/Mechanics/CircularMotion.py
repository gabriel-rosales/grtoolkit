import math
from grtoolkit.Math import solveEqs

################################ RADIAL

def a_rad(printEq=False, **kwargs):
    """
    Usage: radial acceleration (direction is towards axis of rotation)

    Variables: 
        v_rad=radial velocity
        r = radius
        w = magnitude of angular velocity (w_z)"""
    find="a_rad"
    eq = list()
    eq.append("Eq(a_rad, v_rad**2/r)")
    eq.append("Eq(a_rad, w**2*r)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def v_rad(r,T):
    """
    Usage: velocity for uniform circular motion

    Variables: 
        T = period
        r = radius"""
    return 2*math.pi*r/T

################################ TANGENTIAL

# def v_tan():
#     """
#     Usage: velocity for uniform circular motion

#     Variables: 
#         r = radius
#         w = radius"""
#     return r*w


################################ ANGULAR

def w_z(theta, t):
    """
    Usage: angular velocity

    Variables: 
        theta = angle
        t = time"""
    return theta/t

def a_z(w, t):
    """
    Usage: angular acceleration

    Variables: 
        w_z = angular velocity
        t = time"""
    return w/t

def KinematicsAngularEq(find, printEq=False, warning=True, **kwargs):
    """variables: 
                theta, theta0 = angle, initial angle
                w_z, w0_z = angular velocity, initial angular velocity
                a_z = angular acceleration (constant only in this case)
                t = time

        Usage: Energy Applied on an object"""
    if warning:
        print("Note: KineticsAngularEq() is valid for constant angular acceleration (a_z) only")
    eq = list()
    eq.append("Eq(theta, theta0 + w0_z*t + 0.5*a_z*t**2)")
    eq.append("Eq(theta - theta0, 0.5*(w_z + w0_z)*t)")
    eq.append("Eq(w_z, w0_z + a_z*t)")
    eq.append("Eq(w_z**2, w0_z**2 + 2*a_z*(theta - theta0))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)