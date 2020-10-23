from grtoolkit.Math import solveEqs

def Resistance(find, printEq=False, **kwargs):
    """variables: 
                R=resistance
                p=density
                l=length
                A=cross sectional area"""
    eq = list()
    eq.append("Eq(R,p*l/A)")    
    return solveEqs(eq, find, printEq=printEq, **kwargs)
    
def ResistorsInSeries(r_list):
    """Resistors connected in series is the sum of the individual resistances"""
    return sum(r_list)

def ResistorsInParallel(r_list):
    sumOfInverse = sum([1/r for r in r_list])
    return 1/sumOfInverse