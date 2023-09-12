
#Funcion por recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def reverse(num):
    #Inicializa variable donde se almacenará el reverso
    rev_num = 0 
    while num != 0:
        #Extrae el ultimo digito
        digit = num % 10
        #Actualiza la variable
        rev_num = rev_num *10 + digit

        #num = num // 10
        
        #print statement
        #Entender la lógica con digit y num
        
        #print(f'digit: {digit}')
        #print(f'num  : {num}')
            
    #print statement
    #print('Salio del While!')
    

    return rev_num


if __name__ == '__main__':
    #Calcula el factorial
    f = factorial(7)
    print(f'El factorial es: {f}')

    #Invierte el numero
    number = 1234
    rev = reverse(number)
    print(f'Numero: {number} y su inversión: {rev}')