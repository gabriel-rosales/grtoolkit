import math, numpy as np

def roundSig(x, sig=5):
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def softmax(L):
    '''Function that takes as input a list of numbers, and returns the list of values given by the softmax function.'''
    return [np.exp(x)/sum(np.exp(L)) for x in L]

def sigmoid(x):
    return 1/(1+np.exp(-x))