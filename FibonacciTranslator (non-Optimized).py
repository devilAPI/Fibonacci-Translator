print("Welcome to Fibonacci Translator!")
number = int(input("Enter your Number: "))
def translatenumber(n):
    if n == 1 or n == 0:
        return n
    elif n > 1:
        r1 = translatenumber(n-1)
        r2 = translatenumber(n-2)
        return r1 + r2
print(translatenumber(number))
