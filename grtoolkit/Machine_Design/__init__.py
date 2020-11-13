import grtoolkit.Machine_Design.Fasteners

from grtoolkit.Math import solveEqs

def sigma(find="sigma", printEqs=True, **kwargs):
    """
    Stress

    Where:
        sigma = stress
        P = load
        A0 = original cross-sectional area
    """
    eq = list()
    eq.append("Eq(sigma, P / A)")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def stress(find="sigma", printEqs=True, **kwargs):
    return sigma(find="sigma", printEqs=True, **kwargs)

def strain(find="epsilon", printEqs=True, **kwargs):
    """
    Change in length per unit length

    Where:
        epsilon = strain
        l, l0 = length, original length
    """
    eq = list()
    eq.append("Eq(epsilon, (l-l0)/l0)")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def epsilon(find="epsilon", printEqs=True, **kwargs):
    return strain(find="epsilon", printEqs=True, **kwargs)

def modulusOfElasticity(find="epsilon", printEqs=True, **kwargs):
    """
    Defines the slope of the stress-strain curve up to the elastic limit of the material.
    For most ductile materials it is the same in compression as in tensions. Not true for cast irons, other brittle materials, or magnesium.

    Where:
        E = modulus of elasticity
        sigma = stress
        epsilon = strain
    """
    eq = list()
    eq.append("Eq(E, sigma / epsilon")
    eq.append("Eq(E, stress / strain")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def E(find="E", printEqs=True, **kwargs):
    return modulusOfElasticity(find="E", printEqs=True, **kwargs)

def modulusOfRigidity(find="G", printEqs=True, **kwargs):
    """
    Defines the slope of the stress-strain curve up to the elastic limit of the material.
    For most ductile materials it is the same in compression as in tensions. Not true for cast irons, other brittle materials, or magnesium.

    Where:
        E = modulus of elasticity
        v = poisson's ratio

        Material v
        Aluminum    0.34
        Copper      0.35
        Iron        0.28
        Steel       0.28
        Magnesium   0.33
        Titanium    0.34
    """
    eq = list()
    eq.append("Eq(G, E / (2*(1+v))")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def G(find="G", printEqs=True, **kwargs):
    return modulusOfElasticity(find="G", printEqs=True, **kwargs)

def S_us(find="S_us", printEqs=True, **kwargs):
    """
    Ultimate Shear Strength
    Breaking strength in torsion

    Where:
        E = modulus of elasticity
        sigma = stress
        epsilon = strain
    """
    eq = list()
    eq.append("Eq(S_us, T*r/J")
    eq.append("Eq(S_us, 0.80*S_ut") #Approximation; If material == "Steel"
    eq.append("Eq(S_us, 0.75*S_ut") #Approximation; If material == "other ductile material"
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def S_ys(find="S_ys", printEqs=True, **kwargs):
    """
    Shear Yield Strength
    Breaking strength in torsion

    Where:
        S_ys = shear yield strength
    """
    eq = list()
    eq.append("Eq(S_ys, 0.577*Sy") #Approximation
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

def U0(find="U_0", printEqs=True, **kwargs):
    """
    Strain energy density
    Energy absorbtion capacity if a load is suddenly applied. 

    Where:
        U0 = strain energy density per unit volume
        sigma = stress
        epsilon = strain
    """
    eq = list()
    eq.append("Eq(U_0, integrate(sigma,(sigma,0,epsilon))") #Approximation
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

# def UR(find="UR", printEqs=True, **kwargs):
#     """
#     Strain energy density
#     Energy absorbtion capacity if a load is suddenly applied. 

#     Where:
#         U0 = strain energy density per unit volume
#         sigma = stress
#         epsilon = strain
#     """
#     eq = list()
#     eq.append("Eq(U0, integrate(sigma,(sigma,0,epsilon))") #Approximation
#     return solveEqs(eq, find=find, printEq=printEqs, **kwargs)