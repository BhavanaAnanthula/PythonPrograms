def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
a=int(input("enter any number:"))
print(factorial(a))
