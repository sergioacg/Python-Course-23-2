

#Super clase - clase padre
class ComponentesElectronicos:

    #Método constructor
    def __init__(self, nombre, precio, voltaje, corriente):
        self.nombre = nombre
        self.precio = precio
        self.voltaje = voltaje
        self.corriente = corriente

    #Nétodo de instancia
    def obtener_precio(self):
        return self.precio
    
    def obtener_informacion(self):
        print(f'Nombre: {self.nombre}\nPrecio: {self.precio}\nVoltaje: {self.voltaje}\
              \ncorriente: {self.corriente}')
        
#Clase hija - Subclase
class Resistor(ComponentesElectronicos):

    def __init__(self, nombre, precio, voltaje, corriente, tolerancia):
        super().__init__(nombre, precio, voltaje, corriente)
        self.tolerancia = tolerancia

    #Método de instancia
    @property
    def valor_resistencia(self):
        return self.voltaje / self.corriente #Ley de Ohm
    
class Capacitor(ComponentesElectronicos):

    def __init__(self, nombre, precio, voltaje, corriente, tiempo):
        super().__init__(nombre, precio, voltaje, corriente)
        self.tiempo = tiempo

    @property
    def valor_capacitancia(self):
        return self.corriente * self.tiempo / self.voltaje


if __name__ == '__main__':
    componente = ComponentesElectronicos('Integrado', 50, 5, 1)
    componente.obtener_informacion()

    resistor1 = Resistor('Resistor 1/4W', 2, 10, 0.5, 0.05)
    print(f'El precio del resistor es {resistor1.obtener_precio()}')
    print(f'La resistividad es: {resistor1.valor_resistencia}')

    capacitor1 = Capacitor('Capacitor cerámico', 100, 10, 1.5, 0.02)
    print(f'La capacitancia: {capacitor1.valor_capacitancia}')
    capacitor1.obtener_informacion()






