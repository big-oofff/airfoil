import sympy as sp

# Define the variables
y, x = sp.symbols('y x')

# Define the integrand
integrand = sp.sqrt(1 + (10 * y / (25 - x))**2)

# Define the limits of integration for y
y_lower = 0
y_upper = 5 - x / 5

# Compute the integral symbolically
L_top = sp.integrate(integrand, (y, y_lower, y_upper))

print("Symbolic Expression for L_top:")
print(L_top)
