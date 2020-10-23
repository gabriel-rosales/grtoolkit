
import sys

def InSeries(g_list):
    sumOfInverse = sum([1/g for g in g_list])
    return 1/sumOfInverse

def InParallel(g_list):
    return sum(g_list)

#callable function for the module:
class MyModule(sys.modules[__name__].__class__):
    # Replaces
    # def Conductance(r):
    #     return 1/r
    def __call__(self, r): #conductance
        """
        Inverse of Resistance; measured in Siemens.
        """
        return 1/r 
sys.modules[__name__].__class__ = MyModule