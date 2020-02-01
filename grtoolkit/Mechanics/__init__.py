# CONNECT LIBRARIES
import grtoolkit.Mechanics.CircularMotion
import grtoolkit.Mechanics.Friction
import grtoolkit.Mechanics.Kinematics
import grtoolkit.Mechanics.ProjectileMotion
import grtoolkit.Mechanics.Pulleys

# EASY ACCESS
import math, scipy.constants
from grtoolkit.Math import algebraSolve

def magnitude(*args):
    square_sum = 0
    for arg in args:
        square_sum += arg**2
    return math.sqrt(square_sum)
     

def forceEq(find, **kwargs):
    """variables: f=force, m=mass, a=acceleration"""
    return algebraSolve("Eq(f,m*a)", find, **kwargs)

def weight(mass,gravity):
    return mass*gravity

if __name__ == "__main__":
    pass
