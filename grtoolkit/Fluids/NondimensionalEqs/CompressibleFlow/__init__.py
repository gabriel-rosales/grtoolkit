from grtoolkit.Math import solveEqs

def mach(find="Ma", printEqs=True, **kwargs):
    """
    Mach Number = Flow Speed / Sound Speed
    """
    
    eq = list()
    eq.append("Eq(Ma, U/a)")
    return solveEqs(eq, find=find, printEq=printEqs, **kwargs)