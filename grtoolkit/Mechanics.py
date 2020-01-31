import math
from math import radians, degrees
import scipy

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
    for arg in *args:
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
    eq.append("Eq(v, v0 + a*t)")
    eq.append("Eq(d, d0 + v0*t + 0.5*a*t**2)")
    eq.append("Eq(d, d0 + v*t - 0.5*a*t**2)")
    eq.append("Eq(v**2, v0**2 + 2*a*d)")
    
    solution = solveEqs(eq, find, **kwargs)
    
    if printEq:
        print("Equations"), printEquations(eq), print("\n")
        print("Solutions"), printEquations(solution), print("\n")
    return solution

def projectileMotionEq(find, g=scipy.constants.g, angleUnit="radians", printEq=False, **kwargs):
    """variables: 
            x=position-along-x, y=position-along-y,
            alpha0=original trajectory angle,
            t=time, g=standard acceleration of gravity
            vx=velocity-along-x, vy=velocity-along-y"""
    # If degree provided, convert to radians to equations then convert answer to degrees
    alpha0 = radians(alpha0) if angleUnit=="degrees" else alpha0
    # x = (v0*math.cos(alpha0))*t
    # y = (v0*math.sin(alpha0))*t - 0.5*g*t**2
    # vx = v0*cos(alpha0)
    # vy = v0*sin(alpha0)-g*t

    # if find=alpha0 then convert to degrees

def projectileMotion2D(v0, alpha0, t, g=scipy.constants.g, angleUnit="radians"):
    """variables: 
            x=position-along-x, y=position-along-y,
            alpha0=original trajectory angle,
            t=time, g=standard acceleration of gravity
            vx=velocity-along-x, vy=velocity-along-y
    Returns x,y,vx,vy"""
    alpha0 = radians(alpha0) if angleUnit=="degrees" else alpha0
    x=algebraSolve("Eq(x,(v0*math.cos(alpha0))*t)","x",v0=v0, alpha0=alpha0, t=t, g=scipy.constants.g)
    y=algebraSolve("Eq(y,(v0*math.sin(alpha0))*t - 0.5*g*t**2)","y",v0=v0, alpha0=alpha0, t=t, g=scipy.constants.g)
    vx=algebraSolve("Eq(vx,v0*cos(alpha0))","vx",v0=v0, alpha0=alpha0, t=t, g=scipy.constants.g)
    vy=algebraSolve("Eq(vy,v0*sin(alpha0)-g*t","vy",v0=v0, alpha0=alpha0, t=t, g=scipy.constants.g)
    # x = (v0*math.cos(alpha0))*t
    # y = (v0*math.sin(alpha0))*t - 0.5*g*t**2
    # vx = v0*cos(alpha0)
    # vy = v0*sin(alpha0)-g*t   
    return x,y,vx,vy

print(x,y,)



