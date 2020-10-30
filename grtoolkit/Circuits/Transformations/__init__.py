def vSource2cSource(v_s,R):
    """
    Voltage source with resistor in series replaced by 
    current source with resistor in parallel.
    """
    i_s = v_s / R
    return i_s

def cSource2vSource(i_s,R):
    """
    Voltage source with resistor in series replaced by 
    current source with resistor in parallel.
    """
    v_s = i_s * R
    return v_s

def theveninTheorem(Vth, Rth, Rl):
    """
    In practice that a particular element in a circuit is variable
    (usually called the load) while other elements are fixed.
    Each time the variable element
    is changed, the entire circuit has to be analyzed all over again.
    
    Thevenin's theorem states that a linear two-terminal circuit can be
    replaced by an equivalent circuit consisting of a voltage Vth
    in series with a resistor Rth.

    Where VTh is the open-circuit voltage (v_oc) at the
    terminals and RTh is the input or equivalent resistance at the terminals
    when the independent sources are turned off (R_in).
    
    Theory:
        Case 1 (no dependent sources):
        Turn off all independent sources.
        Rth is the input resistance between terminals A & B.
    
        Case 2 (dependent sources):
        This method uses superposition.
        Turn off all independent sources.
        Apply a voltage (v_o; to determine the current) or current (i_o; to determine the voltage) as necessary.
        It can be any value, even 1V or 1A. 
        The result will be the same.
        Rth = v_o/i_o

        Note: having dependent current means that you could end up with a negative Rth. This means that the circuit is actually supplying power.

    Variables:
        Vth = Thevenin Equivalent Voltage
        Rth = Thevenin Equivalent Resistance
        Rl = Load Resistance
        
    Ouput:
        Val1, Val2
    """
    Il = Vth / (Rth + Rl)
    Vl = Rl * Il
    return Vl, Il

def nortonTheorem():
    """
    A linear two terminal circuit can be replaced by an equivalent circuit consisting of a current source I_N in parallel with a resistor R_N.

    Source transformation reveals that:
    R_N = Rth

    Also I_N equals the short-circuit current (i_sc)

    Solve the same way as thevenin's theorem. This is why source transformation is often called Thevenin-Norton transformation.

    """
    pass