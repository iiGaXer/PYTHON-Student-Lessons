import numpy as np
from random import randint

def Array():
    Ex = np.array([randint(1, 10), 5, 1])

    print(Ex.shape)
    print(Ex[0])

#! With library
def num_Array():
    Empty = np.zeros((10, 10))
    print(Empty)

    Values = np.full((3, 3), 127)
    print(Values)

    Random = np.random.random((3,3))
    print(Random)

num_Array()