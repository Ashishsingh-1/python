num = int(input("Enter the last number: "))
current = 1
row = 1

while current <= num:
    for i in range(row):
        if current > num:
            break
        print(current, end=" ")
        current += 1
    print()
    row += 1
