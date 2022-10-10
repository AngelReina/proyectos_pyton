#crear una funcion cuya fib(6)=13

def fibbonacci_rec(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return fibbonacci_rec(n-2)+fibbonacci_rec(n-1)
        return fibbonacci_rec(n)

n= int(input("Dime un número: "))
print(fibbonacci_rec(n))