from sympy import symbols, solve

if __name__ == '__main__':
    a,b,c,x = symbols('a b c x')
    print(solve(x**3 + a* (x**2) + b*x + c, x))

