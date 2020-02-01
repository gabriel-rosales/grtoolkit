from grtoolkit.Math import solveEqs

def kinematicsEq(find, printEq=False, **kwargs):
    """variables: 
                d=distance, d0=initial distance, 
                v=velocity, v0=initial velocity, 
                a=acceleration, 
                t=time"""
    eq = list()
    eq.append("Eq(d, v*t)")
    eq.append("Eq(v, v0 + a*t)")                #constant x-acceleration only
    eq.append("Eq(d, d0 + v0*t + 0.5*a*t**2)")  #constant x-acceleration only
    eq.append("Eq(d, d0 + v*t - 0.5*a*t**2)")
    eq.append("Eq(v**2, v0**2 + 2*a*d)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)