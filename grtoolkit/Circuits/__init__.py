import grtoolkit.Circuits.Filters
import grtoolkit.Circuits.Transistors

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
    eq.append("Eq(i,(v_higher-v_lower)/R)")
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

def currentDivision(i_in, r_branch_list_ordered, showWork=False):
    conductances = [Conductance(r) for r in r_branch_list_ordered]
    g_total = sum(conductances)
    currents = [g/g_total*i_in for g in conductances]
    if showWork:
        print("Branch ordered current division: ", currents) 
    return currents

def Conductance(r):
    return 1/r

def ConductanceInSeries(g_list):
    return ResistorsInParellel(g_list)

def ConductanceInParellel(g_list):
    return ResistorsInSeries(g_list)

def delta2wye(Ra, Rb, Rc):
    Rt = Ra+Rb+Rc
    R1 = Rb*Rc/Rt
    R2 = Rc*Ra/Rt
    R3 = Ra*Rb/Rt
    return R1, R2, R3

def wye2delta(R1, R2, R3):
    Rx = R1*R2 + R2*R3 + R3*R1
    Ra = Rx/R1
    Rb = Rx/R2
    Rc = Rx/R3
    return Ra, Rb, Rc

def NodalSimpleAnalysis(vh, vl, r):
    """Current flows from a higher potential to a lower potential in a resistor"""
    i = (vh-vl)/r
    return i

def NodalAnalysis(find="i", printEq=False, **kwargs):
    """variables: 
            i = current
            vh, vl = higher/lower voltage
            r = resistor
        usage:
            Current flows from a higher potential to a lower potential in a resistor"""
    eq = list()
    eq.append("Eq(i,(v_higher-v_lower)/r)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def supernode():
    print("""
        A supernode is formed by enclosing a (dependent or independent)
        voltage source connected between two nonreference nodes and any
        elements connected in parallel with it.""")

def meshAnalysis():
    # Revisit when simultaneous eq in grtoolkit.math complete
    print("""
        Sum of all voltages in a node""")


