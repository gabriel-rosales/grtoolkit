from sympy import pi

def Period(w):
    """w = angular frequency"""
    T = 2 * pi / w
    return T

def cyclicFrequency(w):
    return Period(w)

def w(f):
    return 2*pi*f

if __name__ == "__main__":
    pass

