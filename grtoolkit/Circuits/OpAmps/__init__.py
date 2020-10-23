# An op amp is an active circuit element designed to perform mathematical operations of addition, subtraction, multiplication, division, differentiation, and integration.

from grtoolkit.Math import solveEqs

def referenceMaterial():
    #Open reference material
    pass

def invertingAmplifier(find="v_out", printEq=False, **kwargs):
    """variables
                v_out, v_in = voltage out/in
                R2, R1 = resistors (view reference image)
    """
    eq = list()
    eq.append("Eq(v_out,-R2/R1*v_in)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def nonInvertingAmplifier(find="v_out", printEq=False, **kwargs):
    """variables: 
                v_out, v_in = voltage out/in
                R2, R1 = resistors (view reference image)
                """
    eq = list()
    eq.append("Eq(v_out,(1+R2/R1)*v_in)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def voltageFollower(find="v_out", printEq=False, **kwargs):
    """variables: 
                v_out, v_in = voltage out/in (view reference image)
                """
    eq = list()
    eq.append("Eq(v_out,v_in)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def summer(find="v_out", printEq=False, **kwargs):
    """variables: 
                v_out, v1, v2, v3 = voltage out/in 
                Rf, R3, R2, R1 = resistors (view reference image)
                """
    eq = list()
    eq.append("Eq(v_out,-(Rf/R1*v1 + Rf/R2*v2 + Rf/R3*v3))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def differenceAmplifier(find="v_out", printEq=False, **kwargs):
    """variables: 
                v_out, v1, v2, v3 = voltage out/in 
                R2, R1 = resistors (view reference image)
                """
    eq = list()
    eq.append("Eq(v_out,R2/R1*(v2-v1)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def DAC(Rf,R_list, V_list):
    """
    TO BE COMPLETED; this can use the summer function. It's the same thing.
    """
    eq = list()
    eq.append("Eq(-v_out,rf/r1*v1 + rf/r2*v2 + rf/r3*v3 + rf/r4*v4")
    # return solveEqs(eq, find, printEq=printEq, **kwargs)

def gainAmplifier():
    """
    TO BE COMPLETED
    """
    eq = list()
    eq.append("Eq(vo,Av*(v2-v1)")
    eq.append("Eq(Av = 1 + 2*R / R_G")