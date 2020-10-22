from grtoolkit.Math import magnitude
from math import pi
def CoulombsLaw(q1, q2, r):
    """Force due to an electric field"""
    epsilon0 = 8.854e-12 #C**2/N*m**2
    k=1/(4*pi*epsilon0)
    F=k*abs(q1*q2)/r**2
    return F

def ElectricForce(q, r):
    """Electric Force at any distance"""
    epsilon0 = 8.854e-12 #C**2/N*m**2
    k=1/(4*pi*epsilon0)
    E = k*abs(q)/r**2
    #Also E=F0/q0
    return E


if __name__ == "__main__":
    a = CoulombsLaw(1e-9,#C
                5e-9,#C
                .02)#m

    # epsilon0 = 8.854*10**-12 #C**2/N*m**2
    # k=1/(4*pi*epsilon0)
    print(a)


