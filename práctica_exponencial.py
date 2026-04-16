import numpy as np
import matplotlib.pyplot as plt

lower_limit = 0
upper_limit = 2
rectangles = 10

def f(x):
    return np.exp(x)

delta_x = (upper_limit - lower_limit) / rectangles
total_area = 0

for i in range(1, rectangles + 1):
    currrent_x = lower_limit + (i - 0.5) * delta_x
    total_area += f(currrent_x) * delta_x

print(total_area)