# ask the user for their name, address and number. Add that info to a dictionary
# Iterate over the info to show the user

Name= input("Please insert your name here: ")
Address= input("Please insert your address here: ")
Number=int(input("Please insert your phone number here: "))

data={}
data['name'] = Name
data['address']=Address
data['number']=Number


for info in data.items():
    print(info)