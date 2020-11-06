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
# z = x + jy            RECTANGULAR FORM
# z = r*angle(phase)    POLAR FORM
# z = r*exp(j*phase)    EXPONENTIAL FORM
# j = (-1)**.5
# r = (x**2 + y**2)**(1/2)
# phi = tan-1(y/x)
# x = r*cos(phi)
# y = r*cos(phi)

# z = x + jy = r*angle(phi) = r*(cos(phi) + j*sin(phi))
# Addition and subtraction are better performed in rectangular form
# Multiplication and division are better done in polar form

# Addition:
# z1 + z2 = (x1 + x2) + j(y1 + y2)

# Subtraction
# z1 - z2 = (x1 - x2) + j(y1 - y2)

# Multiplication:
# z1*z2 = r1*r2 ang(phi1 + phi2)

# Division:
# z1/z2 = r1/r2 ang(phi1-phi2)

# Reciprocal
# 1/z = 1/r ang(-phi)

# Square Root
# sqrt(z) = sqrt(r) ang(phi/2)

# Complex Conjugate
# z* = x-j*y = r ang(-phi) = r*exp(-j*phi)

# Note:
# 1/j = -j
# exp(+/-j*phi) = cos(phi) +/- j*sin(phi)
# cos(phi) = Re( exp(j*phi))
# sin(phi) = Im(exp(j*phi))


# USE cmath? http://ibiblio.org/kuphaldt/socratic/model/mod_phasor.pdf
# >>> from math import *
# >>> from cmath import *
# >>> r = complex(400,0)
# >>> f = 60.0
# >>> xc = 1/(2 * pi * f * 4.7e-6)
# >>> zc = complex(0,-xc)
# >>> xl = 2 * pi * f * 1.0
# >>> zl = complex(0,xl)
# >>> r + zc + zl
# (400-187.38811239154882j)
# >>> 1/(1/r + 1/zc + 1/zl)
# (355.837695813625+125.35793777619385j)
# >>> polar(r + zc + zl)
# (441.717448903332, -0.4381072059213295)
# >>> abs(r + zc + zl)
# 441.717448903332
# >>> phase(r + zc + zl)
# -0.4381072059213295
# >>> degrees(phase(r + zc + zl))
# -25.10169387356105


if __name__ == "__main__":
    pass

