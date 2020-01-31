import math
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

    def projectileMotion(v0, angle, time):
        x = v0*math.cos(math.radians())

