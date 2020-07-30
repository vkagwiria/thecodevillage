# Ask for a number, n.
# Calculate the sum of the numbers before n including the number n
# positive numbers 

n = int(input("Enter a number: "))

sum = 0
counter = 1 # 4,3,2,1

while counter <= n:
    sum = sum + counter
    counter = counter + 1
    
print(sum)

