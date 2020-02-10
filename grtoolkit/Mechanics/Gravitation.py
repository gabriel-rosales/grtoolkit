from grtoolkit.Python import dictionary_add_modify
from grtoolkit.Math import solveEqs
from math import pi
import scipy.constants

def gravitationAttraction(find="F_g", printEq=False, **kwargs):
    """variables:
            F_g = force of attraction due to gravity
            G = 6.67e-11 N*m**2/kg**2
            m1, m2 = mass1, mass2
            r = distance between masses"""
    dictionary_add_modify(kwargs,G=6.67e-11)
    eq = list()
    eq.append("Eq(F_g,G*m1*m2/r**2)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def gravitationalPotentialEnergy(find="U", printEq=False, **kwargs):
    """variables:
            U = gravitational potential energy
            G = 6.67e-11 N*m**2/kg**2
            m1, m2 = mass1, mass2
            r = distance between masses"""
    dictionary_add_modify(kwargs,G=6.67e-11)
    eq = list()
    eq.append("Eq(U,-G*m1*m2/r)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def orbitVelocity(find="v_orb", printEq=False, **kwargs):
    """variables:
            v_orb = gravitational potential energy
            G = 6.67e-11 N*m**2/kg**2
            m_planet=mass of planet being orbited
            r=distance from center of planet being orbited"""
    dictionary_add_modify(kwargs,G=6.67e-11)
    eq = list()
    eq.append("Eq(v,(G*m_planet/r)**(1/2))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def v_orb(find="v_orb", printEq=False, **kwargs):
        return orbitVelocity(find, printEq, **kwargs)

def orbitPeriod(r,v_orb):
        T= 2*pi*r/v_orb
        return T

def blackHoleMaxRadius(M):
        """If a nonrotating spherical mass distribution with total mass M has a radius less than its Schwarzschild radius Rs, it is called a black hole. The gravitational interaction prevents anything including light, from escaping from within a sphere with Radius Rs."""
        G=scipy.constants.G
        c=scipy.constants.c
        Rs=2*G*M/c**2
        return Rs
