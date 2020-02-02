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
     
def forceEq(find, printEq=False, **kwargs):
    """variables: 
                W=Work  F=force  p=momentum  t=time
                x, x0, x1 = distance, start, finish
        Usage: Energy Applied on an object"""
    eq = list()
    eq.append("Eq(F,m*a)")
    eq.append("Eq(F,k*x)")
    eq.append("Eq(F,p/t)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def momentumEq(find, printEq=False, **kwargs):
    """variables: 
                m=mass  v=velocity
        Usage: Energy Applied on an object
        Sample Units: Kg*m/s"""
    eq = list()
    eq.append("Eq(p,m*v)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def impulseEq(find, printEq=False, **kwargs):
    """variables: 
                J=impulse  p1,p2=initial,final momentum
                F=sum of all forces
                t,t0,t1 = time initial,final
        Usage: The change in momentum of a particle during a time interval
        Sample Units: Kg*m/s"""
    eq = list()
    eq.append("Eq(J,p2-p1)")
    eq.append("Eq(J,integrate(F,(t,t0,t1)))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def weight(m,g=scipy.constants.g):
    """variables: m=mass  g=gravitational acceleration constant (9.81 m/s**2)"""
    return m*g

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

