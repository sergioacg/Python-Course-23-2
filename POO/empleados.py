

class Empleados:
    """
    Clase es empleada para representar a un empleado en la empresa
    """

    #Método constructor (método de instancia)
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    #Método de instancia
    def obtener_nombre_completo(self):
        return self.nombre + ' ' + self.apellido
    
    def obtener_salario_anual(self):
        return self.salario * 12
    
    def aumentar_salario(self, porcentaje):
        self.salario *=  (1 + porcentaje/100)

    def __str__(self):
        return f'Nombre: {self.nombre} \nApellido: {self.apellido} \nSalario: {self.salario}'
    
    
#Instanciar el objeto
empleado1 = Empleados('Sergio', 'Giraldo', 5000)
print(f'El nombre del empleao es {empleado1.obtener_nombre_completo()}')
print(f'El salario anual es {empleado1.obtener_salario_anual()}')
empleado1.aumentar_salario(5)
print(f'El salario después de aumentarlo quedó en {empleado1.salario}')

print(empleado1)
