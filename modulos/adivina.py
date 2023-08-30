import random

def main():
    number = random.randint(1, 100)
    intentos = 10
    for i in range(intentos):
        num_user = int(input('Adivina mi número: '))
        if num_user < number:
            print('No, piensa en uno más grande')
        elif num_user > number:
            print('No, piensa en uno más pequeño')
        else:
            print("Felicidades. Ganaste!!")
            break
    if num_user != number:
        print("Perdiste")


#Entry point
if __name__ == '__main__':
    main()