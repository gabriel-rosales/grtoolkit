from sympy import pi

def screwThreadEngagement(diameter, screw="steel", substrate="aluminium"):
    if substrate == "aluminium":
        return 2*diameter
    if substrate == "steel" or substrate == "iron" or substrate == "brass" or substrate == "bronze":
        return 2*diameter

def A_t(find="A_t", printEqs=True, **kwargs):
    """
    Tensile Stress Area

    Where:
        A_t = Tensile Stress Area
        dp, dr = pitch diameter, root diameter
    """
    eq = list()
    eq.append("Eq(A_t, pi/4*((d_p + d_r)/2)**2)") #Approximation
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)



