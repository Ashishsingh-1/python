def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b) 

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
result = lcm(a, b)
print(result)
