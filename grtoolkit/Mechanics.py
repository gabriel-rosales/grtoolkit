import math
from math import radians, degrees
import scipy.constants
from sympy import diff
from grtoolkit.Python import dictionary_add_modify

# from sympy import *
# from grtoolkit.Math import *
from grtoolkit.Math import solveEqs, printEquations, algebraSolve

def minPulleys(load_weight, pull_weight, Safety_factor, exact=False):
### Pull_weight = load_weight/(2**(n-1)) where load_weight is the heavier load.
    # You can use any base for the exp or log functions. The more used are 2, e and 10.
    # https://www.researchgate.net/post/Why_log_with_base_e_is_frequently_used_as_compared_to_base_10
    if exact:
        return math.log(load_weight/pull_weight)/math.log(2)
    return math.ceil(math.log(load_weight/pull_weight)/math.log(2))

def magnitude(*args):
    for arg in args:
        square_sum += arg**2
    return math.sqrt(square_sum)
     

def forceEq(find, **kwargs):
    """variables: f=force, m=mass, a=acceleration"""
    return algebraSolve("Eq(f,m*a)", find, **kwargs)

def kinematicsEq(find, printEq=False, **kwargs):
    """variables: 
                d=distance, d0=initial distance, 
                v=velocity, v0=initial velocity, 
                a=acceleration, 
                t=time"""
    eq = list()
    eq.append("Eq(d, v*t)")
    eq.append("Eq(v, v0 + a*t)")                #constant x-acceleration only
    eq.append("Eq(d, d0 + v0*t + 0.5*a*t**2)")  #constant x-acceleration only
    eq.append("Eq(d, d0 + v*t - 0.5*a*t**2)")
    eq.append("Eq(v**2, v0**2 + 2*a*d)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def projectileMotionEq(find=False, angleUnitRadians=True, printEq=False, **kwargs):
    """variables: 
            x=position-along-x, y=position-along-y,
            alpha0=original trajectory angle,
            t=time, g=standard acceleration of gravity
            vx=velocity-along-x, vy=velocity-along-y
            
        Note:
            Angle solution in radians"""

    if not(angleUnitRadians):
        dictionary_add_modify(kwargs,alpha0=radians(kwargs["alpha0"]))
    if not("g" in kwargs):
        dictionary_add_modify(kwargs,g=scipy.constants.g)

    posx="v0*cos(alpha0)*t"
    posy="v0*sin(alpha0)*t - 0.5*g*t**2"
    eq = list()
    eq.append(f"Eq(x,{posx})")
    eq.append(f"Eq(y,{posy})")
    eq.append(f"Eq(vx,diff({posx},t))")
    eq.append(f"Eq(vy,diff({posy},t))")
    eq.append(f"Eq(ax,diff({posx},t,t))")
    eq.append(f"Eq(ay,diff({posy},t,t))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def projectileMotion2D(v0, alpha0, t, angleUnitRadians=True):
    """Quick version of projectile motion
    returns [x,y,vx,vy]"""
    g = scipy.constants.g
    alpha0 = radians(alpha0) if not(angleUnitRadians) else alpha0
    x=(v0*math.cos(alpha0))*t
    y=(v0*math.sin(alpha0))*t - 0.5*g*t**2
    vx=v0*math.cos(alpha0)
    vy=v0*math.sin(alpha0)-g*t
    return x, y, vx, vy

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

if __name__ == "__main__":
    pass


