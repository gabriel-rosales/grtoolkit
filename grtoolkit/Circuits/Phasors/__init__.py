from sympy import pi

# General expression for sinusoid:
# v(t) = Vm*sin(w*t + phi)
# where,
# phi = phase

# If comparing two sinusoids phase1 != phase2 then "out of phase". 
# One sinusoid leads or lags by phase in radians or degrees.
# If phase difference = 0 then "in phase"


# Trigonometric identities:
# sin(A +/- B) = sinAcosB +/- cosAsinB
# cos(A +/- B) = cosAcosB -/+ sinAsinB

# With these identities, it is easy to show that:
# sin(wt +/- 180 degrees) = -sin(wt)
# cos(wt +/- 180 degrees) = -cos(wt)
# sin(wt +/- 90 degrees) = +/-cos(wt)
# cos(wt +/- 90 degrees) = -/+sin(wt)

# Adding
# A*cos(w*t) + B*sin(w*t) = C*cos(w*t-phase)
# C = (A**2+B**2)**(1/2)
# phase = tan-1(B/A)

# Example:
# 3*cos(wt) - 4*sin(w*t) = 5*cos(wt + 53.1)

def T(w):
    """
    Period
    w = angular frequency
    
    Theory:
    v(t + T) = v(t)
    """
    T = 2 * pi / w
    return T

def f(w):
    """Cyclic frequency"""
    return T(w)

def w(f):
    """Angular frequency"""
    return 2*pi*f

# A complex number can be written in rectangular form as 
# z = x + jy = r*angle(phase) = r*exp(j*phase)
# j = (-1)**.5

if __name__ == "__main__":
    pass

