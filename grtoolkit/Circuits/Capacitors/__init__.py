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

def DC():
    print("Open circuit at DC. Either charging or powering.")

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
    eq.append("Eq(v,(1/C)*integrate(i,(t,ti,tf))+v0)")
    eq.append("Eq(i,C*dv/dt)")
    eq.append("Eq(i,C*diff(v,t))")
    eq.append("Eq(p,v*i)")
    eq.append("Eq(p,C*v*diff(v,t))")
    eq.append("Eq(w,(C*v**2)/2)") 
    eq.append("Eq(w,integrate(C*v,(v,v0,v1)))")
    eq.append("Eq(w,q**2/(2*C))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def delta2wye(Ca, Cb, Cc):
    """
    ''------CA-------''''C2'''''''''C3''''
    '''dd''''''''dd'''''''' y'''''y'''''''
    '''''CC''''CB''''''''''''''y''''''''''
    '''''''d''d''''''''''''''''y''''''''''
    ''''''''dd'''''''''''''''''C1'''''''''

    Returns C1, C2, C3
    """
    Ct = (1/Ca)+(1/Cb)+(1/Cc)
    C1 = 1 / ((1/Cb)*(1/Cc)/Ct)
    C2 = 1 / ((1/Cc)*(1/Ca)/Ct)
    C3 = 1 / ((1/Ca)*(1/Cb)/Ct)
    return C1, C2, C3

def wye2delta(C1, C2, C3):
    """
    ''------CA-------''''C2'''''''''C3''''
    '''dd''''''''dd'''''''' y'''''y'''''''
    '''''CC''''CB''''''''''''''y''''''''''
    '''''''d''d''''''''''''''''y''''''''''
    ''''''''dd'''''''''''''''''C1'''''''''

    Returns Ca, Cb, Cc
    """
    Cx = (1/C1)*(1/C2) + (1/C2)*(1/C3) + (1/C3)*(1/C1)
    Ca = 1 / (Cx/(1/C1))
    Cb = 1 / (Cx/(1/C2))
    Cc = 1 / (Cx/(1/C3))
    return Ca, Cb, Cc

if __name__ == "__main__":
    Value(find="v", printEq=True,
            C=.05,       #Farads
            i=".004*t",   #A
            v0=10,        #V
            ti=0,
            tf="t")        

