import cmath  # Import the complex math module for handling complex roots

def find_quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = (b**2) - (4*a*c)

    # Calculate the two solutions
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return root1, root2

# Coefficients of the quadratic equation
a = 1  # Coefficient of x^2
b = -3  # Coefficient of x
c = 2  # Constant term

# Find the roots of the quadratic equation
root1, root2 = find_quadratic_roots(a, b, c)

# Print the roots
print("Root 1:", root1)
print("Root 2:", root2)
