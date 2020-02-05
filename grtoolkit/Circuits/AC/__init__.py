from grtoolkit.Math import solveEqs

def Capacitor(find, printEq=False, **kwargs):
    """
    usage: capacitor is an open circuit to DC
           voltage cannot change arumptly in a capacitor

    variables: 
                q=charge
                C=capacitance
                v, v0, v1=voltage initial, final
                epsilon = permitivity of the dielectric material between plates
                """
    eq = list()
    eq.append("Eq(q,C*v)")    
    eq.append("Eq(C,epsilon*A*d)")
    eq.append("Eq(w,0.5*C*v**2)") # if capacitor previously discharged
    eq.append("Eq(w,integrate(C*v,(v,v0,v1)))")
    eq.append("Eq(w,q**2/(2*C))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)