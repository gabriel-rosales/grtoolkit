def pressureInFluid(f_perpendicular, A):
    """
    variables:
            f_perpendicular = normal force
            A = area"""
    p=f_perpendicular/A
    return p

def bulkStress(dp, dV, V0):
    """variables:
            dp=change in fluid pressure
            dV=change in subject volume
            V0=original subject volume"""
    # B = bulk stress / bulk strain
    B = dp/(dV/V0)
    return B
