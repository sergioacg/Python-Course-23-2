

class Empleados:
    """
    Clase es empleada para representar a un empleado en la empresa
    """

    #Método constructor (método de instancia)
    def __init__(self, nombre, apellido, salario):
        #Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    #Método de instancia
    @property
    def obtener_nombre_completo(self):
        return self.nombre + ' ' + self.apellido
    
    #Solo lectura
    @property
    def obtener_salario_anual(self):
        return self.salario * 12
    
    #Colocarle la capacidad de ser de escritura
    @obtener_salario_anual.setter
    def obtener_salario_anual(self, nuevo_salario):
        if nuevo_salario < 0:
            raise ValueError('El salario no puede ser negativo')
        self.salario = nuevo_salario / 12

    
    def aumentar_salario(self, porcentaje):
        self.salario *=  (1 + porcentaje/100)

    def __str__(self):
        return f'Nombre: {self.nombre} \nApellido: {self.apellido} \nSalario: {self.salario}'
    
    #Métodos estáticos
    @staticmethod
    def imprimir_informacion():
        print('Esta clase Sirve para controlar la nómina de mi empresa')

    @staticmethod
    def imprimir_nombre(nombre):
        print(f'El nombre de entrada es {nombre}')

    #Variable estática
    empleados = [] #Base de datos de mis empleados

    #Métodos de Clase
    @classmethod
    def agregar_empleado(cls, empleado):
        cls.empleados.append(empleado)
    
    @classmethod
    def calcular_salario_promedio(cls):
        if len(cls.empleados) > 0:
            #                  [Variable]   [for varaiable in lista]  [(opcional) condicion]
            total_salarios = sum(empleado.salario  for empleado in cls.empleados)
            promedio = total_salarios / len(cls.empleados)
            print(f'El salario promedio de los epleados es {promedio:.2f}')
        else:
            print('No hay empleados registrados en la lista')


#Instanciar el objeto
empleado1 = Empleados('Sergio', 'Giraldo', 5000)
print(f'El nombre del empleao es {empleado1.obtener_nombre_completo}')
print(f'El salario anual es {empleado1.obtener_salario_anual}')
#empleado1.aumentar_salario(5)
print(f'El salario después de aumentarlo quedó en {empleado1.salario}')
empleado1.salario = 7000
print(f'El nuevo salario es {empleado1.salario}')
empleado1.obtener_salario_anual = 1000000
print(f'El nuevo salario por segunda vez es {empleado1.salario}')

print(empleado1)

Empleados.imprimir_informacion()
Empleados.imprimir_nombre('Kevin')

#Vamos a utilizar los métodos de clase
Empleados.agregar_empleado(empleado1)

empleado2 = Empleados('Laura', 'Pires', 6000)
empleado3 = Empleados('Gabriel', 'Lopez', 2000)

Empleados.agregar_empleado(empleado2)
Empleados.agregar_empleado(empleado3)

Empleados.calcular_salario_promedio()