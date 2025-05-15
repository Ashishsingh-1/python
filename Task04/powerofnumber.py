def power(x, y):
    if y == 0:
        return 1
    
    elif y < 0:
        return 1 / power(x, -y)
    else:
        return x * power(x, y - 1)
    
x = int(input("Enter base (x): "))
y = int(input("Enter exponent (y): "))
result = power(x, y)
print(result)
