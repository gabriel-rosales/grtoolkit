from grtoolkit.Math import solveEqs

# A second-order circuit is characterized by a second-order differen￾tial equation. It consists of resistors and the equivalent of two energy
# storage elements.

# Second, keep in mind that the capacitor voltage is always continuous so that
# v0_plus = v0_minus
# and the inductor current is always continuous so that
# i0_plus = i0_minus

# Theory:
# Draw the equivalent circuit: 
# - Before a switch opens (t<0)
# - When the switch opens (t=0)
# - Significantly after the switch has been opened (t>0)

# Find v0_minus, i0_minus, diff(v0_minus,t), diff(i0_minus,t), v_inf, i_inf

def sourceFreeSeriesEquivalentCircuit(R, C, L, find="i", printEq=True, **kwargs):
    """Works in radians, not degrees"""
    alpha = R / (2 * L)
    w0 = 1 / (L*C)**(1/2)
    s1 = -alpha + (alpha**2 - w0**2)**(1/2)
    s2 = -alpha - (alpha**2 - w0**2)**(1/2)
    # j = (-1)**(1/2)
    # j = complex(1)

    eq = list()
    if alpha > w0:
        print("Overdamped")
        eq.append("Eq(i, A1*exp(s1*t) + A2*exp(s2*t))")
    if alpha == w0: #C=4*L/R**2
        print("Critically Damped")
        eq.append("Eq(i, (A2 + A1*t)*exp(-alpha*t))")
    if alpha < w0:
        # wd = (w0**2 - alpha**2)**(1/2)
        # B1 = A1 + A2
        # B2 = j*(A1 - A2)
        print("Underdamped")
        eq.append("Eq(i, exp(-alpha*t)*(B1*cos(wd*t) + B2*sin(wd*t)))")

    kwargs.update({"wd": "(w0**2 - alpha**2)**(1/2)", "alpha": alpha, "w0":w0, "s1":s1, "s2":s2, "B1": "A1 + A2", "B2": "j*(A1 - A2)"})

    return solveEqs(eq,find="i", printEq=printEq, **kwargs)

def sourceFreeParallelEquivalentCircuit(R, C, L, find="v", printEq=True, **kwargs):
    """Works in radians, not degrees"""
    alpha = 1 / (2*R*C)
    w0 = 1 / (L*C)**(1/2)
    s1 = -alpha + (alpha**2 - w0**2)**(1/2)
    s2 = -alpha - (alpha**2 - w0**2)**(1/2)

    eq = list()
    if alpha > w0:
        print("Overdamped")
        eq.append("Eq(v, A1*exp(s1*t) + A2*exp(s2*t))")
    if alpha == w0: #C=4*L/R**2
        print("Critically Damped")
        eq.append("Eq(v, (A1 + A2*t)*exp(-alpha * t))")
    if alpha < w0:
        print("Underdamped")
        # wd = (w0**2 - alpha**2)**(1/2)
        # B1 = A1 + A2
        # B2 = j*(A1 - A2)
        eq.append("Eq(v, exp(-alpha*t) * (A1*cos(wd*t) + A2*sin(wd*t)))")

    kwargs.update({"wd": "(w0**2 - alpha**2)**(1/2)", "alpha": alpha, "w0":w0, "s1":s1, "s2":s2})
    
    return solveEqs(eq,find="i", printEq=printEq, **kwargs)

def stepResponseSeriesEquivalentCircuit(R, C, L, find="i", printEq=True, **kwargs):
    """Works in radians, not degrees"""
    alpha = R / (2 * L)
    w0 = 1 / (L*C)**(1/2)
    s1 = -alpha + (alpha**2 - w0**2)**(1/2)
    s2 = -alpha - (alpha**2 - w0**2)**(1/2)
    # j = (-1)**(1/2)
    # j = complex(1)

    eq = list()
    if alpha > w0:
        print("Overdamped")
        eq.append("Eq(v, Vs + A1*exp(s1*t) + A2*exp(s2*t))")
    if alpha == w0: #C=4*L/R**2
        print("Critically Damped")
        eq.append("Eq(v, Vs + (A1 + A2*t)*exp(-alpha*t))")
    if alpha < w0:
        # wd = (w0**2 - alpha**2)**(1/2)
        # B1 = A1 + A2
        # B2 = j*(A1 - A2)
        print("Underdamped")
        eq.append("Eq(v, Vs + (A1*cos(wd*t) + A2*sin(wd*t)) * exp(-alpha*t))")

    kwargs.update({"wd": "(w0**2 - alpha**2)**(1/2)", "alpha": alpha, "w0":w0, "s1":s1, "s2":s2, "B1": "A1 + A2", "B2": "j*(A1 - A2)"})

    return solveEqs(eq,find="i", printEq=printEq, **kwargs)

def stepResponseParallelEquivalentCircuit(R, C, L, find="i", printEq=True, **kwargs):
    """Works in radians, not degrees"""
    alpha = R / (2 * L)
    w0 = 1 / (L*C)**(1/2)
    s1 = -alpha + (alpha**2 - w0**2)**(1/2)
    s2 = -alpha - (alpha**2 - w0**2)**(1/2)
    # j = (-1)**(1/2)
    # j = complex(1)

    eq = list()
    if alpha > w0:
        print("Overdamped")
        eq.append("Eq(i, Is + A1*exp(s1*t) + A2*exp(s2*t))")
    if alpha == w0: #C=4*L/R**2
        print("Critically Damped")
        eq.append("Eq(i, Is + (A1 + A2*t)*exp(-alpha*t))")
    if alpha < w0:
        # wd = (w0**2 - alpha**2)**(1/2)
        # B1 = A1 + A2
        # B2 = j*(A1 - A2)
        print("Underdamped")
        eq.append("Eq(i, Is + (A1*cos(wd*t) + A2*sin(wd*t))*exp(-alpha*t))")

    kwargs.update({"wd": "(w0**2 - alpha**2)**(1/2)", "alpha": alpha, "w0":w0, "s1":s1, "s2":s2, "B1": "A1 + A2", "B2": "j*(A1 - A2)"})

    return solveEqs(eq,find="i", printEq=printEq, **kwargs)





if __name__ == "__main__":
    sourceFreeSeriesEquivalentCircuit(5,6e-3,8)


