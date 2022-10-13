import random

num_random=random.randint(1,100)
print("Este juego consiste en que vas a tener que adivinar un numero entre el 1 y 100, pero solo tienes 3 oportunidades")
vidas=3
while(vidas>0):
    num_usuario= int(input("Dime un número: "))
    if(num_usuario!=num_random):
        vidas=vidas-1
        if(vidas!=1):
            print("Te quedan",vidas,"oportunidades")
        else:
            print("Te quedan",vidas,"oportunidad")
    else:
        print("Has acertado el número")
        break

if (vidas==0):
    print("El numero era:",num_random)