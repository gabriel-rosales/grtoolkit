import grtoolkit.Circuits.AC
import grtoolkit.Circuits.Capacitors as Capacitors
import grtoolkit.Circuits.Conductance as Conductance
import grtoolkit.Circuits.Filters
import grtoolkit.Circuits.Inductors as Inductors
import grtoolkit.Circuits.OpAmps
import grtoolkit.Circuits.Resistors as Resistors
import grtoolkit.Circuits.Transformations
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

def KVL(eq):
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
        elements connected in parallel with it.
        
        Short circuit the two nodes.""")

def supermesh():
    print("""
        A supermesh results when two meshes have a (dependent or independent)
        current source in common.
        
        Short circuit the two meshes.""")

def superposition():
    """
    Alternative to nodal analysis if circuit has two or more independent sources.
    Determine the contribution of each independent source and add them up.
    The idea of superposition rests on the linearity property. 
    As the input increases linearly so does the output.
    
    The voltage across (or current through) an element in a linear circuit is the 
    algebraic sum of the voltages across (or current through) that element due to 
    each independent source acting alone.
    
    Theory:
        1. Turn off all independent sources expect one source.
        Find the output (voltage or current) due to that active source using KVL & KCL

        2. Repeat for each independent source.

        3. Find the total contribution by adding algebraically all the contributions due to the independent sources.
    """
    pass

def maximumPowerTransfer(Rth, Rl, Vth):
    """
    Maximum power is delivered to a system when the load resistance (Rl) equals the Thevenin resistance (Rth).
    """
    if Rth == Rl:
        pmax = Vth**2 / 4 * Rth
        return pmax
    else:
        p = (Vth / (Rth + Rl))**2 * Rl
        return p

if __name__ == "__main__":
    # eq = list()
    # eq.append("(v1-24)/250+(v1/50)+(v1-60*ib)/150")
    # eq.append("Eq(ib,(24-v1)/250)")
    # print(KCL(eq))
    # [{ib: 48/605, v1: 504/121}]

    # eq = list()
    # eq.append("Eq(-15+5*i1+10*(i1-i2)+10,0)")  # Mesh 1 Equation
    # eq.append("6*i2+4*i2+10*(i2-i1)-10")       # Mesh 2 Equation
    # solveSimultaneousEqs(eq)

    # print(KCL(eq))

    pass