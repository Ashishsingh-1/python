def gcd(a, b):

    if b == 0:
        return abs(a) #absolute value
    else:
        return gcd(b, a % b)
    
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
result = gcd(a, b)
print(result)
