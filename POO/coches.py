

class Coche:
    """
    Docstrings: Esta clase sirve para trabajar con coches
    Recuerde que es una clase de Juguete
    """
    tiene_motor = True

    #Método Constructor
    def __init__(self, marca, modelo, color = 'Plata'):
        self.marca_del_carro = marca
        self.modelo = modelo
        self.color = color

    #Método Destructor
    def __del__(self):
        print('El coche ha sido destruido')


audi = Coche('Audi', 'A4', 'Negro') #Creado - Instanciado el Primero Objeto
otro_coche = Coche('Renault', 'Logan', 'Verde')

print(dir(audi))
print(audi.__dict__)
print(audi.marca_del_carro)
print(audi.tiene_motor)
del audi
print(audi.color)

