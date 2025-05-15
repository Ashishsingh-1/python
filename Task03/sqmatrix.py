n = int(input("Enter the size of the square matrix: "))
count = 1

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(0, end=" ")
            count += 1
        else:
            print(count, end=" ")
            count += 1
    print()
