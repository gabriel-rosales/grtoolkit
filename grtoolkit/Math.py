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
    '''Sample inputs: Y=[1,1,0] and P=[0.8,0.7,0.1] Equal 0.69
    Where,
    Y is list of whether events are on or off
    P is list of probabilities if events are on
    
    Formula is sum of all cases of entropy if event is active plus entropy if event is inactive
    
    Events with high probabilities have low cross entopy
    Events with low proabilities have high cross entropy

    OR

    High cross entropy means low probability
    Low cross entropy means high probability
    '''
   
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

w1 = 3; w2=5; b=-2.2
x = sigmoid(w1*.4 + w2*.6 + b)
print(x)