
import sympy as sp

# Define variable
x = sp.Symbol('x')

# Define function
f = x**2 + 3*x + 2

# Calculate integration
result = sp.integrate(f, (x, 0, 2))

print("Integration result:", result)
print("Decimal result:", result.evalf())
