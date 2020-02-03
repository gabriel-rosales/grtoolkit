from grtoolkit.Math import solveEqs

#UNTESTED

def Value(find, printEq=False, **kwargs):
    """
    variables: 
        Fs=simple future value,
        F=compound future value, 
        P=present value, 
        A=annuity (repeated payment)
        N=number of periods (ex. if 15yrs semiannually, N=30), 
        i_simple=simple interest,
        G=gradient, 
        i_growth=growth adjusted interest
        g=rate of growth
    """
    eq = list()
    eq.append("Eq(Fs,P*i_simple*N")
    eq.append("Eq(F,P*(1+i_simple)**N)")
    eq.append("Eq(A,F/N)") if kwargs["i_simple"] == 0 else eq.append("Eq(A,F*(i_simple/((1+i_simple)**N-1)))")
    eq.append("Eq(A,P*(i_simple*(1+i_simple)**N/((1+i_simple)**N-1)))")
    eq.append("Eq(A,G*1/i_simple-N/((1+i_simple)**N-1)")
    eq.append("Eq(P,A*((1+i_growth)**N-1)/(i_growth*(1+i_growth)**N)*(1/(1+g)))")   
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def i_simple(r,m):
    """
    variables: 
        r=nominal interest rate
        m=number of periods in a year
            Ex. annually = 1
                semianually = 2
                quaterly = 4
    """
    return r/m

def i_growth(i_simple,g):
    """
    variables: 
        g=rate of growth
    """
    return (1+i_simple)/(1+g)-1

def i_eff(printEq=False, **kwargs):
    """
    variables: 
        i_eff=effective interest
        r=
        m=

    """
    find="i_eff"
    eq = list()
    eq.append("Eq(i_eff,((1+r/m)**m)-1)")
    eq.append("Eq(i_eff,((1+i_simple)**m)-1)")
    eq.append("Eq(i_eff,exp(r)-1)")             #continuous
    return solveEqs(eq, find, printEq=printEq, **kwargs)

