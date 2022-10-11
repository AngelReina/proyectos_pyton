# Decir si un numero es primo CON FUNCION



def esPrimo(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True


def primeros1000primos_for():
    lst = []
    for i in range(1,1001):
        if(esPrimo(i)):
            lst.append(i)
    return lst
  
def primeros1000primos_while():
    i = 1
    lst = []
    
    while(i < 1000):
        if(esPrimo(i)):
            lst.append(i)
        i = i + 1
    return 