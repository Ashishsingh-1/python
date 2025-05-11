totalsum = 0

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        totalsum += num

print("The sum of all numbers divisible by 3 and 7 up to 100 is:", totalsum)
