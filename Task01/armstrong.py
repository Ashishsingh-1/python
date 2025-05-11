num = int(input("Enter the number: "))
n = len(str(num))
temp = num
sum = 0
while num>0:
    digit = temp%10
    sum+=digit**n
    temp=temp//10
if num==sum:
        print("This is the armstrong number: ", num)
else:
        print("This is not an armstrong number: ")
