#  Write a program that prints all the numbers from 0 to 6 except 3 and 6.


for num in range (0,7):  
    if num == 0:
        continue  
    elif num == 6:
        continue 
    print(num)