import math, scipy.constants
from grtoolkit.Math import solveEqs
from grtoolkit.Python import dictionary_add_modify

def projectileMotionEq(find=False, angleUnitRadians=True, printEq=False, **kwargs):
    """variables: 
            x=position-along-x, y=position-along-y,
            alpha0=original trajectory angle,
            t=time, g=standard acceleration of gravity
            vx=velocity-along-x, vy=velocity-along-y
            
        Note:
            Angle solution in radians"""

    if not(angleUnitRadians):
        dictionary_add_modify(kwargs,alpha0=radians(kwargs["alpha0"]))
    if not("g" in kwargs):
        dictionary_add_modify(kwargs,g=scipy.constants.g)

    posx="v0*cos(alpha0)*t"
    posy="v0*sin(alpha0)*t - 0.5*g*t**2"
    eq = list()
    eq.append(f"Eq(x,{posx})")
    eq.append(f"Eq(y,{posy})")
    eq.append(f"Eq(vx,diff({posx},t))")
    eq.append(f"Eq(vy,diff({posy},t))")
    eq.append(f"Eq(ax,diff({posx},t,t))")
    eq.append(f"Eq(ay,diff({posy},t,t))")
    return solveEqs(eq, find, printEq=printEq, **kwargs)

def projectileMotion2D(v0, alpha0, t, angleUnitRadians=True):
    """Quick version of projectile motion
    returns [x,y,vx,vy]"""
    g = scipy.constants.g
    alpha0 = radians(alpha0) if not(angleUnitRadians) else alpha0
    x=(v0*math.cos(alpha0))*t
    y=(v0*math.sin(alpha0))*t - 0.5*g*t**2
    vx=v0*math.cos(alpha0)
    vy=v0*math.sin(alpha0)-g*t
    return x, y, vx, vy