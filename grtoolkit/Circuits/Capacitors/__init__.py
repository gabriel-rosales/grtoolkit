from grtoolkit.Math import solveEqs

#Designed to store energy in its electric field.

# Capacitors do not dissipate, but store or release energy
# Capacitors are used to block dc, pass ac, shift phase, store energy, start motors, and suppress noise.
# A capacitor is an open circuit to dc
# The voltage across a capacitor must be continuous. It cannot cange abruptly.
# The capacitor resists an abrupt change in voltage across it.
# It is not physically possible for the capacitor voltage to take the form
# Conversely, the current through a capacitor can change instantaneously.
# The ideal capacitor does not dissipate energy. It takes power from
# the circuit when storing energy in its field and returns previously
# stored energy when delivering power to the circuit.
# A real, nonideal capacitor has a parallel-model leakage resistance.
# The leakage resistance may be as high as 100 MOhms and can be neglected for most practical applications.

def Capacitance(find="C", printEq=False, **kwargs):
    """
    Usage: the ratio of the charge on one plate of a capacitor to the voltage difference between the two plates, measured in farads (F).

    Variables: 
                C = capacitance (1 Farads = 1 Coulomb/Volt)
                epsilon = permitivity of the dielectric material between plates
                A = surface area of each plate
                d = distance between plates"""
    eq = list()
    eq.append("Eq(C,epsilon*A/d)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def InSeries(c_list):
    sumOfInverse = sum([1/c for c in c_list])
    return 1/sumOfInverse

def InParallel(c_list):
       return sum(c_list)

def Value(find, printEq=False, **kwargs):
    """
    usage: capacitor is an open circuit to DC
           voltage cannot change abrumptly in a capacitor

    Variables: 
                q=charge
                C=capacitance
                v, v0, v1=voltage initial, final
                epsilon = permitivity of the dielectric material between plates
                w=work
                A = cross-sectional area
                d = distance between plates

    Equations:
            q = C * v
            C = epsilon * A * d
            i = C * dv/dt
            p = v * i
            p = C * v * dv/dt
            w = 0.5 * C * v**2
            w = integrate(C * v, (v,v0,v1))
            w = q**2 / (2 * C)
    """
    eq = list()
    eq.append("Eq(q,C*v)")    
    eq.append("Eq(C,epsilon*A*d)")
    eq.append("Eq(i,C*dv/dt)")
    eq.append("Eq(p,v*i)")
    eq.append("Eq(p,C*v*dv/dt)")
    eq.append("Eq(w,0.5*C*v**2)") 
    eq.append("Eq(w,integrate(C*v,(v,v0,v1)))")
    eq.append("Eq(w,q**2/(2*C))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)