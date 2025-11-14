from sympy import symbols, factor

x = symbols('x')
print(factor(x**3- 3*x**2 + 3*x - 1))
