import math, numpy as np

def roundSig(x, sig=5):
    if x == 0:
        return 0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

def softmax(L):
    '''Function that takes as input a list of numbers, and returns the list of values given by the softmax function.
    
    Example:
    Input [1,2,3]
    Output [e**1/(e**1 + e**2 + e**3),
            e**2/(e**1 + e**2 + e**3)
            e**3/(e**1 + e**2 + e**3)]'''
    return [np.exp(x)/sum(np.exp(L)) for x in L]

def sigmoid(x):
    return 1/(1+np.exp(-x))

def cross_entropy(Y, P):
    '''Sample inputs: Y=[1,0,1,1] and P=[0.4,0.6,0.1,0.5]
    Where,
    Y is list of whether events are on or off
    P is list of probabilities if events are on
    
    Formula is sum of all cases of entropy if event is active plus entropy if event is inactive'''
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

def multi_class_cross_entropy():
    pass