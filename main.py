import numpy as np

# Challenge 1

# Original array
array = np.arange(0,21)


r1 = np.mean(array)
r2 = np.std(array)
r3 = np.var(array)

print(array)
print("Mean: ", r1)
print("Std: ", r2)
print("Variance: ", r3)
