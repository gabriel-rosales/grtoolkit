from sympy import symbols, Piecewise, diff, integrate

def step(t0=0, **kwargs):
    return u(t0, **kwargs)

def u(t0=0, **kwargs):
    """
    Unit Step Function

    Usage:
        For u(t):
            u()

        For u(t-3):
            u(-3)

        For u(t+2) @ t=7:
            u(t0=2, t=7)
    """
    t = symbols("t")

    # t0 = -t0
    func = Piecewise((0, t<-t0), 
                     (1, t>-t0))

    if kwargs:
        for k,v in kwargs.items():
            func = func.subs(k,v)
    return func

def impulse(t0=0, **kwargs):
    return d(t0, **kwargs)

def d(t0=0, **kwargs):
    """
    Unit Impulse Function

    d(t) is zero everywhere excelt at t=-t0 where it is undefinded (nan).

    Usage:
        For d(t):
            d()

        For d(t-3):
            d(-3)

        For d(t+2) @ t=7:
            d(t0=2, t=7)

    """
    t = symbols("t")
    func = diff(u(t0),t)
    if kwargs:
        for k,v in kwargs.items():
            func = func.subs(k,v)
    return func   


def ramp(t0=0, **kwargs):
    return r(t0, **kwargs)

def r(t0=0, **kwargs):
    """
    Unit Ramp Function

    d(t) is zero for negative values of t and has a unit slope for positive values of t.

    Usage:
        For r(t):
            r()

        For r(t-3):
            r(-3)

        For r(t+2) @ t=7:
            r(t0=2, t=7)

    """
    t = symbols("t")
    func = integrate(u(t0),t)
    if kwargs:
        for k,v in kwargs.items():
            func = func.subs(k,v)
    return func   

if __name__ == "__main__":
    print(step(t0=5,t=-4))

