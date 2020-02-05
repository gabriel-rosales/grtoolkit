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

def KCL(i_list):
    """Sum of currents entering a node equal the sum of currents leaving a node"""
    return sum(i_list)

def KVL(v_list):
    """Sum of all voltages around a closed path (or loop) is 0"""
    return sum(v_list)

def ResistorsInSeries(r_list):
    """Resistors connected in series is the sum of the individual resistances"""
    return sum(r_list)

def ResistorsInParellel(r_list):
    sumOfInverse = sum([1/r for r in r_list])
    return 1/sumOfInverse

def voltageDivision(v_in, r_list_ordered, showWork=False):
    """voltage is divided among the resistors in direct proportion to their resistances; the larger the resistance, the larger the voltage drop."""
    r_total = sum(r_list_ordered)
    voltages = [r/r_total*v_in for r in r_list_ordered]
    print("Resistor ordered voltage division: ", voltages)
    return voltages

