
#import sys
#sys.path.append('C:\\Users\\Sergio\\My Drive\\Clases\\Programación 2\\Python')
import functions.funciones as ff

#print(sys.path)
print("Hola Mundo!")

base_usuario = 7
altura_usuario = 4

area = ff.area_rectangulo(base_usuario, altura_usuario)

print(f'El area del rectangulo es {area}, cuya base es {base_usuario}, y altura es {altura_usuario}')
