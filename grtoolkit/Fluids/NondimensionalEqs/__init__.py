from grtoolkit.Math import solveEqs

def reynolds(find="Re", printEqs=True, **kwargs):
    """
    Reynolds Number = Inertia / Viscosity
    """
    
    eq = list()
    eq.append("Eq(Re, rho * U * L / mu)")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)

# ref white pg 307