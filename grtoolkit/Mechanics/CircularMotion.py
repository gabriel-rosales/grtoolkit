import math
from grtoolkit.Math import solveEqs
from grtoolkit.Mechanics import magnitude

################################ RADIAL
def v_rad(r,T):
    """
    Usage: velocity for uniform circular motion

    Variables: 
        T = period
        r = radius"""
    return 2*math.pi*r/T

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


################################ TANGENTIAL

def v_tan(r, w_z):
    """
    Usage: velocity for uniform circular motion

    Variables: 
        r = radius
        w = magnitude of angular velocity (w_z)"""
    return r*magnitude(w_z)

def a_tan(find="a_tan", printEq=False, **kwargs):
    """
    Usage: radial acceleration (direction is towards axis of rotation)

    Variables: 
        a_tan=tangential acceleration
        dv=change in velocity
        dw=change in angular velocity
        dt=change in time
        r=radius
        alpha=rate of change of angular velocity
        """
    eq = list()
    eq.append("Eq(a_tan, dv/dt)")
    eq.append("Eq(a_tan, r*dw/dt)")
    eq.append("Eq(a_tan, r*alpha)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)


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

def KinematicsRotationalEq(find, printEq=False, warning=True, **kwargs):
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

################################ MOMENT OF INERTIA 
################################ KINETIC ENERGY

def momentOfInertia(m_r_touple_list):
    """
    Sample Input [(mass1, radius1), ..., (mass2, radius2)]
    
    Variables: 
        mass = mass
        radius = perpendicular distance from axis of rotation
    
    Usage: the higher the moment of inertia, the more 
    difficult it is to change the state of the body's rotation"""
    I = sum([m*r**2 for m,r in m_r_touple_list])
    return I

def kineticEnergy(I, w):
    """
    variables: 
        K = kinetic energy
        I = moment of inertia
        w = magnitude of angular velocity (w_z)
    """
    K=.5*I*w**2
    return K

def torque(find, printEq=False, warning=True, **kwargs):
    """
    variables:
        tau, tau_z = torque, torque along axis z
        F = force
        d = distance
        I = moment of inertia
        dw = change in angular speed
        dL = change in angular momentum
        dt = change in time
        dtheta = change in angle 
    """
    eq = list()
    eq.append("Eq(tau, F*d)")
    eq.append("Eq(tau, I*a_z)")
    eq.append("Eq(W,tau*dtheta)")
    eq.append("Eq(W,.5*I*dw**2)")
    eq.append("Eq(P,tau_z*w_z)")
    eq.append("Eq(dL/dt)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def angularMomentum(find, printEq=False, warning=True, **kwargs):
    eq = list()
    eq.append("Eq(L, I*w)")
    eq.append("Eq(tau, I*a_z)")
    eq.append("Eq(W,tau*dtheta)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)


        
