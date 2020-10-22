import grtoolkit.Circuits.AC
import grtoolkit.Circuits.Filters
import grtoolkit.Circuits.OpAmps
import grtoolkit.Circuits.Transistors
from grtoolkit.Math import solveEqs, solveSimultaneousEqs

## NOTE
# SERIES: Current constant, voltage divides
# PARALLEL: Voltage constant, current divides

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

def Capacitance(find="C", printEq=False, **kwargs):
    """
    Usage: the ratio of the charge on one plate of a capacitor to the voltage difference between the two plates, measured in farads (F).


    variables: 
                C = capacitance
                epsilon = permitivity of the dielectric material between plates
                A = surface area of each plate
                d = distance between plates"""
    eq = list()
    eq.append("Eq(C,epsilon*A/d)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def KCL(eq):
    """
    Conservation of current.
    Sum of currents entering a node equal the sum of currents leaving a node
    
    Theory:
        => Assume current directions & choose reference node (ground)
        => For each relevant node, obtain node equation
        => i1+ i2 = i3 + i4
        => For each current if necessary replace with (vh-vl)/R in direction of travel
        => Solve simultaneous equation for missing values.

    Usage:
        eq = list()
        eq.append("Eq(-v1/10-v1/5-6-(v1-v2)/2,0)") # Node 1 Equation
        eq.append("v2/4-3-6-(v1-v2)/2")            # Node 2 Equation
        solveSimultaneousEqs(eq)

    Output:
        [{v2: 12, v1: 0}]
    """
    return solveSimultaneousEqs(eq)

def KVL(v_list):
    """
    Conservation of Voltage
    Sum of all voltages around a closed path (or loop) is 0

    Theory:
    => Assume current directions & choose reference node (ground)
    => For each mesh, obtain mesh equation
    => -v1 + v2 + v3 + v4 = 0
    => For each voltage, if necessary, replace with i*R in direction of travel
    => Solve simultaneous equation for missing values.

    Usage:
        eq = list()
        eq.append("Eq(-15 + 5*i1 + 10*(i1-i2) + 10, 0)")  # Mesh 1 Equation
        eq.append("6*i2 + 4*i2 + 10*(i2-i1) - 10")        # Mesh 2 Equation
        solveSimultaneousEqs(eq)

    Output:
        [{i2: 1, i1: 1}]
    """
    # TO BE COMPLETED
    return solveSimultaneousEqs(eq)

def ResistorsInSeries(r_list):
    """Resistors connected in series is the sum of the individual resistances"""
    return sum(r_list)

def ResistorsInParellel(r_list):
    sumOfInverse = sum([1/r for r in r_list])
    return 1/sumOfInverse

def voltageDivision(v_in, r_list_ordered, showWork=False):
    """
    Voltage is divided among the resistors in direct proportion to their resistances; 
    the larger the resistance, the larger the voltage drop.
    """
    r_total = sum(r_list_ordered)
    voltages = [r/r_total*v_in for r in r_list_ordered]
    if showWork:
        print("Resistor ordered voltage division: ", voltages)
        print("Adjust directions as necessary after getting result.")
    return voltages

def currentDivision(i_in, r_branch_list_ordered, showWork=False):
    conductances = [Conductance(r) for r in r_branch_list_ordered]
    g_total = sum(conductances)
    currents = [g/g_total*i_in for g in conductances]
    if showWork:
        print("Branch ordered current division: ", currents) 
        print("Adjust directions as necessary after getting result.")
    return currents

def Conductance(r):
    return 1/r

def ConductanceInSeries(g_list):
    return ResistorsInParellel(g_list)

def ConductanceInParellel(g_list):
    return ResistorsInSeries(g_list)

def delta2wye(Ra, Rb, Rc):
    """
    ''------RA-------''''R2'''''''''R3''''
    '''dd''''''''dd'''''''' y'''''y'''''''
    '''''RC''''RB''''''''''''''y''''''''''
    '''''''d''d''''''''''''''''y''''''''''
    ''''''''dd'''''''''''''''''R1'''''''''

    Returns R1, R2, R3
    """
    Rt = Ra+Rb+Rc
    R1 = Rb*Rc/Rt
    R2 = Rc*Ra/Rt
    R3 = Ra*Rb/Rt
    return R1, R2, R3

def wye2delta(R1, R2, R3):
    """
    ''------RA-------''''R2'''''''''R3''''
    '''dd''''''''dd'''''''' y'''''y'''''''
    '''''RC''''RB''''''''''''''y''''''''''
    '''''''d''d''''''''''''''''y''''''''''
    ''''''''dd'''''''''''''''''R1'''''''''

    Returns Ra, Rb, Rc
    """
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
    print("""Sum of all voltages in a node""")

def sourceTransformation():
    # TO BE REVIEWED
    pass

def TheveninNorton():
    # TO BE REVIEWED
    pass

def maximumPowerTransfer():
    # TO BE REVIEWED
    pass

if __name__ == "__main__":
    # eq = list()
    # eq.append("(v1-24)/250+(v1/50)+(v1-60*ib)/150")
    # eq.append("Eq(ib,(24-v1)/250)")
    # print(KCL(eq))
    # [{ib: 48/605, v1: 504/121}]

    eq = list()
    eq.append("Eq(-15+5*i1+10*(i1-i2)+10,0)")  # Mesh 1 Equation
    eq.append("6*i2+4*i2+10*(i2-i1)-10")       # Mesh 2 Equation
    solveSimultaneousEqs(eq)

    # eq.append("Eq(ib,(24-v1)/250)")
    print(KCL(eq))