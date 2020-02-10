# CONNECT LIBRARIES
import grtoolkit.Mechanics.CircularMotion
import grtoolkit.Mechanics.Collisions
import grtoolkit.Mechanics.Friction
import grtoolkit.Mechanics.Kinematics
import grtoolkit.Mechanics.ProjectileMotion
import grtoolkit.Mechanics.Pulleys

# EASY ACCESS
import math, scipy.constants
from grtoolkit.Math import algebraSolve, solveEqs, magnitude
     
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
                J=impulse  
                p1,p2=initial,final momentum
                F=sum of all forces
                t,t0,t1 = time initial,final
        Usage: The change in momentum of a particle during a time interval
        Sample Units: Kg*m/s"""
    eq = list()
    eq.append("Eq(J,p2-p1)")
    eq.append("Eq(J,integrate(F,(t,t0,t1)))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def weight(m,g=scipy.constants.g):
    """variables: m=mass  
                  g=gravitational acceleration constant (9.81 m/s**2)"""
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

def centerOfMass(*args):
    """input: [m, x, y, z, r]
       variables: m=mass, 
                  x=position-along-x, 
                  y=position-along-y, 
                  z=position-along-z, 
                  r=position-along-radius"""
    mi=0; xi=1; yi=2; zi=3; ri=4
    m_total = sum([item[mi] for item in args])
    x = sum([item[mi]*item[xi] for item in args])/m_total
    y = sum([item[mi]*item[yi] for item in args])/m_total
    z = sum([item[mi]*item[zi] for item in args])/m_total
    r = sum([item[mi]*item[ri] for item in args])/m_total
    return x,y,z,r

def centerOfMassMotion(*args):
    """input: [m, vx, vy, vz, vr]
       variables: m=mass, 
                  vx=velocity-along-x, 
                  vy=velocity-along-y, 
                  vz=velocity-along-z, 
                  vr=velocity-along-radius"""
    mi=0; vxi=1; vyi=2; vzi=3; vri=4
    m_total = sum([item[mi] for item in args])
    vx = sum([item[mi]*item[vxi] for item in args])/m_total
    vy = sum([item[mi]*item[vyi] for item in args])/m_total
    vz = sum([item[mi]*item[vzi] for item in args])/m_total
    vr = sum([item[mi]*item[vri] for item in args])/m_total
    return vx,vy,vz,vr

def stress(f_normal,A):
    """variables:
            sigma=stress
            f_normal=force
            a=area"""
    sigma = f_normal/A
    return sigma

def shearStress(f_parallel,A):
    """variables:
            sigma_shear=shear stress (parallel)
            f=force
            a=area"""
    sigma_shear = f_parallel/A
    return sigma_shear
    
def strain(dl,l0):
    """variables:
            epsilon=strain
            dl=change in length
            l0=initial length"""
    epsilon = dl/l0
    return epsilon

def YoungsModulusEq(find="Y", printEq=False, **kwargs):
    """variables: 
            Y=young's modulus of elasticity
            sigma=stress
            epsilon=strain
    """
    eq = list()
    eq.append("Eq(Y, sigma/epsilon)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def shearModulus(find="S", printEq=False, **kwargs):
    """variables: 
            S = shear modulus
            sigma_shear = shear stress
            dx = along shear force (parallel to surface)
            h = height of subject that is subject to shear forces
    """
    eq = list()
    eq.append("Eq(S, sigma_shear/(dx/h))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

if __name__ == "__main__":
    pass