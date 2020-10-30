from grtoolkit.Math import solveEqs

# Designed to store energy in its magnetic field.
# Consists of a coil of inducting wire

# An inductor acts like a short circuit to DC.
# The current through an inductor cannot change instantaneously.


# A discontinuous change in the current through an inductor requires an infinite voltage, which is not physically possible.

# The ideal capacitor, the ideal inductor does not dissipate energy. The energy stored in it can be retrieved at a later time.

# A practical, nonideal inductor has a significant resistive component.
# This resistance is called the winding resistance (R_w) , and
# it appears in series with the inductance of the inductor.
# R_w is usually very small and can be ignored at high frequencies.

# The nonideal inductor also has a winding capacitance (C_w)
# due to the capacitive coupling between the conducting coils.
# C_w is usually negligible except at high frequencies. 

def Value(find, printEq=False, **kwargs):
    """
    usage: 
        measured in Farads (F)
        inductor is an short circuit in DC
        current cannot change abrumptly in a capacitor

    variables: 
        v=voltage
        L=inductance (measured in Henry = Volt/Ampere)
        di=change in current
        t, t0, t1, dt=time, initial time, future time, change in time
        i, i0, di = current, initial current, change in current
        w=work (J)

    Equations:
        v = L * di/dt
        i = 1/L * integrate(v,(t,t0,t1)) + i0
        p = v * i
        p = L * di/dt * i
        w = 0.5 * L * i**2
    """
    eq = list()
    eq.append("Eq(v,L*di/dt)")
    eq.append("Eq(v,L*diff(i,t))")
    eq.append("Eq(i,1/L*integrate(v,(t,t0,t1))+i0)")
    eq.append("Eq(p,v*i)")
    eq.append("Eq(p, L*di/dt*i)")
    eq.append("Eq(w,0.5*L*i**2)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def inductance(find="L", printEq=False, **kwargs):
    """
    Usage: Measured in henry (H = Volt/Ampere)

    variables: 
                N=number of turns
                A=cross sectional area
                l=length
                mu=permeability of core
    """
    eq = list()
    eq.append("Eq(L,N**2*mu*A/l)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def inductorsInSeries(l_list):
    return sum(l_list)

def inductorsInParallel(l_list):
    sumOfInverse = sum([1/l for l in l_list])
    return 1/sumOfInverse
