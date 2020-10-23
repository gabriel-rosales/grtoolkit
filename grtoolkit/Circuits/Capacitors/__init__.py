from grtoolkit.Math import solveEqs

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

def InSeries(c_list):
    sumOfInverse = sum([1/c for c in c_list])
    return 1/sumOfInverse

def InParallel(c_list):
       return sum(c_list)

def Value(find, printEq=False, **kwargs):
    """
    usage: capacitor is an open circuit to DC
           voltage cannot change abrumptly in a capacitor

    variables: 
                q=charge
                C=capacitance
                v, v0, v1=voltage initial, final
                epsilon = permitivity of the dielectric material between plates
                w=work
    """
    eq = list()
    eq.append("Eq(q,C*v)")    
    eq.append("Eq(C,epsilon*A*d)")
    eq.append("Eq(i,C*dv/dt)")
    eq.append("Eq(w,0.5*C*v**2)") 
    eq.append("Eq(w,integrate(C*v,(v,v0,v1)))")
    eq.append("Eq(w,q**2/(2*C))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)