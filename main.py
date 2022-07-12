import numpy as np


def broadcast(a, b):
    return a * b


a = np.array([
    1, 2, 3
])

b = np.array([
    2, 2, 2
])

print(broadcast(a, b))