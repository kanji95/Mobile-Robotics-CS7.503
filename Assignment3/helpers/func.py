import numpy as np
import math

def make_gaussian(x, a, mean, std):
    y = a * (1/(np.sqrt(2 * np.pi) * std)) * np.exp(-(x-mean)**2/(2*std**2))
    return y

def make_non_linear(x, p1, p2, p3, p4):
    y = p1 * math.exp(-x / p2) + p3 * math.sin(x / p4)
    return y
