# Compute Gradient of a scalar field.



import numpy as np

# define the scalar field
def f(x, y, z):
    return x*3 * y * z*2

# define the coordinates at which to evaluate the gradient
x = 1.0
y = 1.0
z = 1.0

# compute the partial derivatives
dfdx = 3 * x*2 * y * z*2
dfdy = x*3 * z*2
dfdz = 2 * x**3 * y * z

# create a numpy array to represent the gradient vector
grad = np.array([dfdx, dfdy, dfdz])

# print the gradient vector
print("The gradient vector at ({}, {}, {}) is {}".format(x, y, z, grad))