import sympy as sym

# Prompt the user to input the function in LaTeX format
latex_function = input("Enter the function in LaTeX (e.g., x^2 + xy^2): ")

# Convert the LaTeX function to a symbolic expression
x, y = sym.symbols('x y')
function_expr = sym.sympify(latex_function)

# Calculate the derivative with respect to x
derivative_expr = sym.diff(function_expr, x)
22
# Evaluate the derivative at a specific point (e.g., x=1, y=1)
derivative_value = derivative_expr.subs({x: 1, y: 1})

print(f"The derivative of the function {latex_function} with respect to x is:")
print(derivative_expr)
print(f"At the point (x=1, y=1), the derivative has a value of {derivative_value:.2f}")
