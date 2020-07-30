# write a program to get the sum of all the numbers in list

def sum(numbers):
    total=0
    for number in numbers:
        total=total+number
    return total

totalsum=sum([1,2,3,4,5,5])

print("The sum is ", totalsum)
