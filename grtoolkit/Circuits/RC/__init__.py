from grtoolkit.Math import solveEqs, algebraSolve
from sympy import symbols, Piecewise, sympify

#Capacitors and inductors are considered fully charged at 5 time constants.

def naturalResponse(find, printEq=True, **kwargs):
    """
    Source-Free

    The natural response of a circuit refers to the behavior (in terms of
    voltages and currents) of the circuit itself, with no external sources of
    excitation.

    v(0) = V0
    
    variables: 
            v_o, v1, v2, v3 = Open loop voltage gain, voltage in
            R2, R1 = resistors (view reference image)

            tau = The time constant; the time required for the response to
            decay to a factor of 1/e or 36.8 percent of its initial value.
    """
    eq = list()
    eq.append("Eq(tau, R_eq * C_eq")
    eq.append("Eq(v, V0 * exp(-t / tau))")
    eq.append("Eq(i_R, v / R")
    eq.append("Eq(i_R, V0 * exp(-t / tau)/R)")
    eq.append("Eq(p, v * i_R")
    eq.append("Eq(p, V0**2 * exp(-2*t / tau)/R)")
    eq.append("Eq(w, integrate(p,(t,0,tf))")
    eq.append("Eq(w, integrate(V0**2 * exp(-2*t / tau) / R, (t,0,tf))")
    eq.append("Eq(w, .5 * C * V0**2 * (1 - exp(-2*t / tau)))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def stepResponse(find = "v",**kwargs):
    """
    The step response of a circuit is its behavior when the excitation is the
    step function, which may be a voltage or a current source.
    """
    eq = "Eq(v,Piecewise((V0, t<-t0), ((Vs + (V0-Vs)*exp(-t/tau)), t>-t0)))"
    return algebraSolve(eq,solve_for=find,**kwargs)

def completeResponse(find = "v",**kwargs):
    eq = list()

    # Complete Response = natural response (stored energy) + forced response (independent source)
    eq.append("Eq(v, v_n + v_f)")
    eq.append("Eq(v_n, V0 * exp(-t / tau))")
    eq.append("Eq(v_f, V_s * (1-exp(-t/tau)))")

    # Complete Response = transient response (temporary part) + steady-state response (permanent part)
    # Transient response is the circuit's temporary response that will die out with time.
    # The steady-state response is the behavior of the circuit a long time after an external excitation is applied.
    eq.append("Eq(v, v_t + v_ss)")
    eq.append("Eq(v_t, (V0-V_s * exp(-t / tau))")
    eq.append("Eq(v_ss, V_s")
    # Or
    eq.append("Eq(v, v_inf + (v0-v_inf) * exp(-t / tau))")
    #  where v_inf = the final voltage of the capacitor, v0 = the initial capacitor voltage, tau = time constant
    return solveEqs(eq, find, printEq=printEq, **kwargs)

if __name__ == "__main__":
    print(stepResponse(find="tau"))