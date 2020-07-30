# Accept n number from user and calculate the sum of all number between 1 and n including n

number = int(input("Please insert your number here: "))
sum = 0
for i in range (1,number+1):
    sum = sum + i
print(sum)

