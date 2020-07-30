# Ask for user input, and write a for loop that will output all the vowels within it. 
# example:
# "Valentine" -> "aei"
# "Wycliffe" -> "ei"

name = input("Please insert your name here: ").lower()
vowels = "aeoui"
for vowel in vowels:
    if vowel in name:
        print(vowel)
# for letter in name:
#     if letter == vowel:
#         print( letter)