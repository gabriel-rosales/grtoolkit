from grtoolkit.Math import solveEqs

def capacitor(find, printEq=False, **kwargs):
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
    eq.append("Eq(i,C*dv/dt)")
    eq.append("Eq(w,0.5*C*v**2)") # if capacitor previously discharged
    eq.append("Eq(w,integrate(C*v,(v,v0,v1)))")
    eq.append("Eq(w,q**2/(2*C))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def capacitorsInSeries(c_list):
    sumOfInverse = sum([1/c for c in c_list])
    return 1/sumOfInverse

def capacitorsInParallel(c_list):
       return sum(c_list)

def inductor(find, printEq=False, **kwargs):
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
    eq.append("Eq(v,L*di/dt)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def inductance(find, printEq=False, **kwargs):
    """variables: 
                N=number of turns
                A=cross sectional area
                l=length
                mew=permeability of core"""
    eq = list()
    eq.append("Eq(L,N**2,mew*A/l)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)