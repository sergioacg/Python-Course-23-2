
nombres = []
for i in range(5):
    nombre = input(f'Ingresa el nombre {i+1}: ')
    nombres.append(nombre)

#imprimir
print(f'Lista original {nombres}')

#Preguntar si va a eliminar
eliminar = input("Desea eliminar algún nombre? (s/n): ")
if eliminar.lower() == 's':
    nombre_eliminar = input("Ingrese el nombre a eliminar: ")
    if nombre_eliminar in nombres:
        nombres.remove(nombre_eliminar)
        print(f'Lista actualizada {nombres}')
    else:
        print("El nombre no se encuentra en la lista")

agregar = input("Desea agregar algún nombre al principio? (s/n): ")
if agregar.lower() == 's':
    nombre_agregar =  input("Ingrese el nombre a adicionar: ")
    nombres.insert(0, nombre_agregar)
    print(f'Lista actualizada {nombres}')

print(f'Longitud de la lista {len(nombres)}')
print('Nombres en posiciones impares: ', end='')
for i in range(0, len(nombres), 2):
    print(nombres[i], end=' ')
