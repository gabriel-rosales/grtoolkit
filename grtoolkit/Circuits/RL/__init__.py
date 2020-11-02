from grtoolkit.Math import solveEqs

#Capacitors and inductors are considered fully charged at 5 time constants.

def naturalResponse(find, printEq=True, **kwargs):
    """
    Source-Free

    The natural response of a circuit refers to the behavior (in terms of
    voltages and currents) of the circuit itself, with no external sources of
    excitation.

    i(0) = I0
    
    variables: 
            v_o, v1, v2, v3 = Open loop voltage gain, voltage in
            R2, R1 = resistors (view reference image)

            tau = The time constant; the time required for the response to
            decay to a factor of 1/e or 36.8 percent of its initial value.
    """
    eq = list()
    eq.append("Eq(tau, L_eq / R_eq")
    eq.append("Eq(w0, .5 * L * I0**2")
    eq.append("Eq(v_L + v_R, 0")
    eq.append("Eq(L * di/dt + R*i, 0")
    eq.append("Eq(L * diff(i,t) + R*i, 0")
    eq.append("Eq(i, I0*exp(-t/tau))")
    eq.append("Eq(v_R, i * R)")
    eq.append("Eq(v_R, I0 * R * exp(-2*t/tau))")
    eq.append("Eq(p, v_R * i)")
    eq.append("Eq(p, I0**2 * R * exp(-2*t/tau))")
    eq.append("Eq(w, integrate(p,(t,0,tf)))")
    eq.append("Eq(w,.5 * L * I0**2 * (1-exp(-2*t/tau)))")

    return solveEqs(eq, find, printEq=printEq, **kwargs)

def completeResponse(find = "i",**kwargs):
    eq = list()
    eq.append("Eq(i, i_inf + (i0-i_inf) * exp(-t / tau))")
    #  where v_inf = the final voltage of the capacitor, v0 = the initial capacitor voltage, tau = time constant
    return solveEqs(eq, find, printEq=printEq, **kwargs)