num = int(input("Enter a number: "))
sumdigits = 0

while num > 0:
    digit = num % 10        
    sumdigits += digit    
    num = num // 10       

print("Sum of digits is:", sumdigits)
