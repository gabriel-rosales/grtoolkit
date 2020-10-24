# An op amp is an active circuit element designed to perform mathematical operations of addition, subtraction, multiplication, division, differentiation, and integration.

from grtoolkit.Math import solveEqs

def referenceMaterial():
    #Open reference material
    pass

def vd(v2,v1):
    """
    Differential voltage
    v1 = voltage between inverting terminal and ground
    v2 = voltage between non-inverting terminal and ground
    """
    return v2-v1

def i_out(i1,i2,i_plus, i_minus):
    """Output current"""
    return sum(i1, i2, i_plus, i_minus)

def v_o(A,vd):
    """
    Open loop voltage gain.
    Gain of the op amp without any external feedback from output to input.
    Sometimes voltage gain (A) is expressed in decibels (dB).
    A dB = 20*log_10(A)

    Usage:
        v_o(4, vd(4,6))
    """
    return A*vd

def mode(v_o, Vcc):
    """
    A practical limitation of the op amp is that the magnitude of its output voltage cannot exceed abs(Vcc).
    The output voltage is dependent on an limited by the power supply voltage.

    Although we shall always operate the op amp in the linear region, the
    possibility of saturation must be borne in mind when one designs with
    op amps, to avoid designing op amp circuits that will not work in the
    laboratory.
    """
    if v_o == Vcc:
        return "positive saturation"
    if v_o >= -Vcc and v_o <= Vcc:
        return "linear region"
    if v_o == -Vcc:
        return "negative saturation"

def idealOpAmp():
    """
    An amplifier with infinite open-loop gain (v_o), infinite input resistance, and zero output resistance.
    Ideal op amp is an approximate analysis, but most modern amplifiers have such large gain and input impedances that the approximate analysis is a good one.

    Characteristics:

    An infinite resistance between the input terminals implies that an open circuit exists there
    and current cannot enter the op amp. But the output current is not necessarily zero.
        i1 = 0
        i2 = 0 # Due to infinite resistance

    The voltage across the input terminals is equal to zero.
    vd = v2 - v2 = 0
    v1 = v2

    A is approx inf
    Ri is approx inf
    Ro is approx 0
    """

def invertingAmplifier(find="v_o", printEq=False, **kwargs):
    """Variables:
                v_o, v_in = Open loop voltage gain, voltage in
                R2, R1 = resistors (view reference image)

        Equation: v_o = -R2/R1 * v_in
    """
    eq = list()
    eq.append("Eq(v_o,-R2/R1*v_in)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def nonInvertingAmplifier(find="v_o", printEq=False, **kwargs):
    """Variables: 
                v_o, v_in = Open loop voltage gain, voltage in
                Rf, R1 = resistors (view reference image)

        Note: If Rf = 0 (short circuit) or R1 is approx. inf or both, then the gain becomes 1.
        Under these conditions the output follows the input and this is known as a voltage follower.

        Such a circuit has very high impedence and therefore useful as an intermediate-stage (or buffer) amplifier to isolate one circuit from another.
        The voltage follower minimizes the interaction between the two stages and eliminates interstage loading.

        Equation: v_o = (1 + Rf/R1) * v_in
    """
    eq = list()
    eq.append("Eq(v_o,(1 + Rf/R1)*v_in)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def summer(find="v_o", printEq=False, **kwargs):
    """variables: 
                v_o, v1, v2, v3 = Open loop voltage gain, voltage in
                Rf, R3, R2, R1 = resistors (view reference image)
                """
    eq = list()
    eq.append("Eq(v_o,-(Rf/R1*v1 + Rf/R2*v2 + Rf/R3*v3))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def differenceAmplifier(find="v_o", printEq=False, **kwargs):
    """variables: 
                v_o, v1, v2, v3 = Open loop voltage gain, voltage in
                R2, R1 = resistors (view reference image)
                """
    eq = list()
    eq.append("Eq(v_o,R2/R1*(v2-v1)")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def DAC(Rf,R_list, V_list):
    """
    TO BE COMPLETED; this can use the summer function. It's the same thing.
    """
    eq = list()
    eq.append("Eq(-v_o,rf/r1*v1 + rf/r2*v2 + rf/r3*v3 + rf/r4*v4")
    # return solveEqs(eq, find, printEq=printEq, **kwargs)

def instrumentationAmplifier():
    """
    For precision measurement and process control
    Applications include: isolation amplifiers, thermocouple amplifiers, and data acquisition systems.
    TO BE COMPLETED
    """
    eq = list()
    eq.append("Eq(vo,A_v*(v2-v1)")
    eq.append("Eq(Av, 1 + 2*R / R_G")