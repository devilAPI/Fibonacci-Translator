print("Welcome to Fibonacci Translator!")
number = int(input("Enter your Number: "))
list = [0,1]
def translatenumber(n):
    if len(list) > n+1:
        return list[n]
    else:
        r1 = translatenumber(n-1)
        r2 = translatenumber(n-2)
        r = r1+r2
        list.insert(n,r)
        return r
print(translatenumber(number))
