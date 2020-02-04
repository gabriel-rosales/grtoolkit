import grtoolkit.Circuits.Filters

from grtoolkit.Math import solveEqs

def BasicLaws(find, printEq=False, **kwargs):
    """variables: 
                V=voltage       (V)
                I=current       (A)
                R=resistance    (ohm) 
                P=power         (W)
                Q=charge        (C)
                G=conductance   (mho aka. siemens)"""
    eq = list()
    eq.append("Eq(V,I*R)")    
    eq.append("Eq(P,V*I)")
    eq.append("Eq(P,W/t)")    
    eq.append("Eq(V,W/Q)")
    eq.append("Eq(I,Q/t)")  
    eq.append("Eq(Q,integrate(I,(t,t0,t1)))")
    eq.append("Eq(G,1/R")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def Resistance(find, printEq=False, **kwargs):
    """variables: 
                R=resistance
                p=density
                l=length
                A=cross sectional area"""
    eq = list()
    eq.append("Eq(R,p*l/A)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)
