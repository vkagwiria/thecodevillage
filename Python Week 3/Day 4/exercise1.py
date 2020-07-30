# Write a while loop that continues to ask for user input and runs
# until they type “quit”.


user_input = True 
while user_input:
    user_input=input("Please insert a word here: ").lower()
    if user_input == "quit":
        user_input = False
        
    
# while (word=""):
#     print(word)
# if word="quit":
#     break
# else:
#     print(word)