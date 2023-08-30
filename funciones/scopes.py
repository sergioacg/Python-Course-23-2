
g = 9.8

def force_newton(mass, aceleration):
    global F
    F = mass * aceleration
    print('newton', F, id(F), sep=' --> ')
    #print('newton', g, id(g), sep=' --> ')

def force_pressure(pressure, area):
    F = pressure * area
    print('pressure', F, id(F), sep=' --> ')
    #print('newton', g, id(g), sep=' --> ')


force_newton(10, 2)
force_pressure(4, 3)
print('global', F, id(F), sep=' --> ')