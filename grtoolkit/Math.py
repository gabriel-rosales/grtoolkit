import math, numpy as np
from sympy import *

def roundSig(x, sig=5):
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def delta(p1,p2):

    return abs(p2-p1)

def softmax(L):
    '''Function that takes as input a list of numbers, and returns the list of values given by the softmax function.
    
    Example:
    Input [1,2,3]
    Output [e**1/(e**1 + e**2 + e**3),
            e**2/(e**1 + e**2 + e**3)
            e**3/(e**1 + e**2 + e**3)]'''
    return [np.exp(x)/sum(np.exp(L)) for x in L]

def sigmoid(x):
    return 1/(1+np.exp(-x))

def cross_entropy(Y, P):
    '''Sample inputs: Y=[1,1,0] and P=[0.8,0.7,0.1] Equal 0.69
    Where,
    Y is list of whether events are on or off
    P is list of probabilities if events are on
    
    Formula is sum of all cases of entropy if event is active plus entropy if event is inactive
    
    Events with high probabilities have low cross entopy
    Events with low proabilities have high cross entropy

    OR

    High cross entropy means low probability
    Low cross entropy means high probability
    '''
   
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

def algebraSolve(expr, solve_for,**kwargs):
    """Solves algebraic string equation. 
    format: algebraSolve("x**2 + 3*x - 1/2 + y", "x", y=24)
    **"""
    expr=sympify(expr)
    #GENERATE VARIABLE SYMBOLS FROM EXPRESSION
    for sym in expr.free_symbols: 
        exec(f"{sym.name}=symbols('{sym.name}')")
        #MAKE solve_for STRING EQUAL REQUIRED EXPRESSION VARIABLE SYMBOL
        if solve_for == sym.name:    
            solve_for = sym
        
        # SUBSTITUTE KARGs FOR EXPRESSION SYMBOLS
        for k, v in kwargs.items():
            if k == sym.name:
                expr=expr.subs(k,v)
    return solve(expr, solve_for)

def solveEqs(eq, find, printEq=False, **kwargs):
    #CREATE SET OF ARGUMENTS SUPPLIED TO FUNCTION
    availSet = {find}
    for k in kwargs.keys():
        availSet.add(k)
    eq = [sympify(expr) for expr in eq]
    freesym = [expr.free_symbols for expr in eq]
    freevar = []
    solution = list()
    #CONVERT LIST OF SETS OF SYMBOLS INTO LIST OF SETS OF STR
    for freeset in freesym:
        tempset = set()
        for sym in freeset:
            tempset.add(sym.name)
        freevar.append(tempset)
    unknowns = [freeset-availSet for freeset in freevar]            # Eliminate variables requested in function arguments: find and knowns
    unknowns_count = [len(unknownset) for unknownset in unknowns]   # How many unknowns are left in each equation?
    find_avail = [find in freevarset for freevarset in freevar]     # Is the variable in question available in this equation?
    index = list(range(len(unknowns_count)))
    zipper = list(zip(index, unknowns_count, find_avail))

    for zippedList in zipper:
        solution.append(algebraSolve(eq[zippedList[0]],find, **kwargs))

    printEquationsSolution(eq, solution) #print Equations and Solutions to console
    return solution

def printEquations(eq):
    # print("Equations:\n")
    for equation in eq:
        print(equation)

def printEquationsSolution(eq, solution, printEq=True):
    #if printEq:
    print("\n")
    print("Equations"), printEquations(eq), print("\n")
    print("Solutions"), printEquations(solution), print("\n")