from grtoolkit.Math import solveEqs

def capacitor(find, printEq=False, **kwargs):
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

def capacitorsInSeries(c_list):
    sumOfInverse = sum([1/c for c in c_list])
    return 1/sumOfInverse

def capacitorsInParallel(c_list):
       return sum(c_list)

def inductor(find, printEq=False, **kwargs):
    """
    usage: 
        measured in Farads (F)
        inductor is an short circuit in DC
        current cannot change abrumptly in a capacitor

    variables: 
        v=voltage
        L=inductance
        di=change in current
        t, t0, t1, dt=time, initial time, future time, change in time
        i, i0, di = current, initial current, change in current
        w=work (J)
    """
    eq = list()
    eq.append("Eq(v,L*di/dt)")
    eq.append("Eq(i,1/L*integrate(v,(t,t0,t1))+i0)")
    eq.append("Eq(w,0.5*L*i**2)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def inductance(find="L", printEq=False, **kwargs):
    """
    usage: measured in henry (H)

    variables: 
                N=number of turns
                A=cross sectional area
                l=length
                mu=permeability of core"""
    eq = list()
    eq.append("Eq(L,N**2,mu*A/l)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def inductorsInSeries(l_list):
    return sum(l_list)

def inductorsInParallel(l_list):
    sumOfInverse = sum([1/l for l in l_list])
    return 1/sumOfInverse