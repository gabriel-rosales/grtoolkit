# CONNECT LIBRARIES
import grtoolkit.Mechanics.CircularMotion
import grtoolkit.Mechanics.Friction
import grtoolkit.Mechanics.Kinematics
import grtoolkit.Mechanics.ProjectileMotion
import grtoolkit.Mechanics.Pulleys

# EASY ACCESS
import math, scipy.constants
from grtoolkit.Math import algebraSolve, solveEqs

def magnitude(*args):
    square_sum = 0
    for arg in args:
        square_sum += arg**2
    return math.sqrt(square_sum)
     

def forceEq(find, **kwargs):
    """variables: F=force, m=mass, a=acceleration"""
    #TO DO: Add eq F=kx
    return algebraSolve("Eq(F,m*a)", find, **kwargs)

def weight(mass,gravity):
    return mass*gravity

def kineticEnergy(mass,velocity):
    """1 J = 1 N*m = 1 Kg*m**2/s**2
    Usage: Energy moving an object"""
    K = 0.5*mass*velocity**2
    return K

def elasticPotentialEnergy(k,x):
    """1 J = 1 N*m = 1 Kg*m**2/s**2
    Variables: k=spring constant   x=distance compressed
    Usage: Energy stored by springs"""
    U = 0.5*k*x**2
    return U   

def gravitationalPotentialEnergy(mass, gravity, y):
    """1 J = 1 N*m = 1 Kg*m**2/s**2
    Variables: m=mass   g=gravity constant   y=height
    Usage: Energy stored by springs"""
    U = mass*gravity*y
    return U       

def workEq(find, printEq=False, **kwargs):
    """variables: 
                W=Work  F=force
                x, x0, x1 = distance, start, finish
        Usage: Energy Applied on an object"""
    eq = list()
    eq.append("Eq(W, F*x)")
    eq.append("Eq(W,integrate(F,(x,x0,x1)))")
    eq.append("Eq(W, P*t)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def powerEq(find, printEq=False, **kwargs):
    """variables: 
                P=power  W=Work  t=time
                f=force  v=velocity
        Base Unit = Watts"""
    eq = list()
    eq.append("Eq(P, W/t)")
    eq.append("Eq(P, F*v)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

if __name__ == "__main__":
    pass

