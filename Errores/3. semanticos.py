"""
Crear una función que sea capaz de encontrar las raíces de una ecuación cuadrática de la forma: 
by: Sergio Andres Castaño Giraldo
"""

def quadratic_equation(a, b, c):
    # calculate the discriminant
    d = (b*2) - (4*a*c)

    # find two solutions
    x1 = (-b-(d)**0.5)/(2*a)
    x2 = (-b+(d)**0.5)/(2*a)
    return x1, x2


if __name__ == '__main__':
    print('Python Program to Solve Quadratic Equation')

    a = float(input('Coefficients a: '))
    b = float(input('Coefficients b: '))
    c = float(input('Coefficients c: '))

    x1, x2 = quadratic_equation(a, b, c)

    print(f'The solution are {x1} and {x2}')