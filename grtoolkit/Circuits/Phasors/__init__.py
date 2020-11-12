from sympy import pi
from math import *
from cmath import *

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
# v(t) = Re(Vm*cos(w*t+phi))
# V is used as the phasor representation of v(t)

class signal:
    """
    Types: "rect" "polar_rad" "polar_deg" 
    https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types
    """
    def __init__(self, val=complex(0,0), format="rect"):
        """
        Types: "rect" "polar_rad" "polar_deg" "wave_deg" "wave_rad"

        Input:
            rect: val = complex(0,0)
            polar_rad = (A,phi_rad)
            polar_deg = (A, phi_deg)
            wave = (A, "cos", w, phi) or (A, "sin", w, phi)

        """

        if format == "rect":
            self.rect = val
        elif format == "polar_rad":
            self.polar_rad = val
        elif format == "polar_deg":
            self.polar_deg = val
        elif "wave" in format:
            self.wave_original = val
            self.wave_original_type = format
            phasor = ()
            val = list(val)
            if "deg" in format:
                val[3] = radians(val[3])
            if val[1] == "cos":
                phasor = self.__cos2Phasor(val[0], val[3])
            elif val[1] == "sin":
                phasor = self.__sin2Phasor(val[0], val[3])
            else:
                raise 'Not a valid sinusoid. Format must be (A, "cos", w, phi) or (A, "cos", w, phi)'
            self.polar_rad = (phasor[0], phasor[1])
        else:
            raise 'type must be: "rect" "polar_rad" "polar_deg"'

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, val):
        self._rect = val
        self._polar_rad = self.__rect2polar(self._rect)
        self._polar_deg = self.__polar_deg_view()

    @property
    def polar_rad(self):
        return self._polar_rad
    @polar_rad.setter
    def polar_rad(self, val):
        self._polar_rad = val
        self._polar_deg = self.__polar_deg_view()
        self._rect = self.__polar2rect(self._polar_rad)

    def __polar_deg_view(self):
        """
        Does not return actual polar as actual polar needs to be in radians. 
        For viewing ONLY.
        """
        polar = self._polar_rad
        polar_fix = list()
        polar_fix.append(polar[0])
        polar_fix.append(degrees(polar[1]))
        return polar_fix

    @property
    def polar_deg(self):
        return self._polar_deg
    @polar_deg.setter
    def polar_deg(self, val):
        self._polar_deg = val
        self._polar_rad = self.__polar_rad_view()
        self._rect = self.__polar2rect(self._polar_rad)

    @property
    def sinusoid(self):
        return self._sinusoid
    @sinusoid.setter
    def sinusoid(self, val):
        self._sinusoid = val

    def __polar2rect(self, r,phi=0):
        """
        Output: class <complex>
        """
        if isinstance(r,tuple) or isinstance(r,list):
            return rect(r[0],r[1])
        return rect(r,phi)

    def __rect2polar(self,z):
        """
        Polar cannot do math.
        Output: class <tuple>
        """
        return polar(z)

    def __polar_rad_view(self):
        """
        Does not return actual polar as actual polar needs to be in radians. 
        For viewing ONLY.
        """
        polar = self._polar_deg
        polar_fix = list()
        polar_fix.append(polar[0])
        polar_fix.append(radians(polar[1]))
        return polar_fix

    def __cos2Phasor(self, A,phi):
        """
        Format: A*cos(wt+phi)
        Output: [A, phi] which represents polar form A angle(phi)
        """
        if A < 0:
            return self.__cos2Phasor(-A, phi+radians(180))
        else:
            return A, phi
    def __sin2Phasor(self, A, phi):
        if A < 0:
            return self.__sin2Phasor(-A, phi+radians(180))
        else:
            return A, phi-radians(90)

    def sin_wave(self, format="rad"):
        if format == "deg":
            return f"{self._polar_rad[0]} sin (wt * {degrees(self.polar_rad[1]-radians(90))})"
        return f"{self._polar_rad[0]} sin (wt * {self.polar_rad[1]-radians(90)})"

    def cos_wave(self, format="rad"):
        if format == "deg":
            return f"{self._polar_rad[0]} cos (wt * {degrees(self.polar_rad[1])})"
        return f"{self._polar_rad[0]} cos (wt * {self.polar_rad[1]})"

    def __add__(self,other):
        return signal(self._rect + other._rect)
    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self,other):
        return signal(self._rect - other._rect)
    def __rsub__(self, other):
        #Doesn't work?
        return other - self._rect

    def __mul__(self,other):
        return signal(self._rect * other._rect)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self,other):
        return signal(self._rect / other._rect)
    def __rtruediv__(self,other):
        # return signal(other / self._rect)
        return other / self._rect

    def __pow__(self,other):
        # return signal(other / self._rect)
        return signal(self.rect**(other))

    def sqrt(self):
        return signal(self.rect**(1/2))

## NOTE: 
# DERIVATIVE 
# dv/dt      ==      jwV
# time domain    frquency domain

# INTEGRAL
# integrate(v,t)    ==    V/jw
# time domain          frquency domain


if __name__ == "__main__":
    z1 = signal((40,50), format="polar_rad")
    z2 = signal((20,-30), format="polar_deg")
