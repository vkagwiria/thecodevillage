firstname = input("Please enter your first name: ")
lastname = input("Please enter your second name: ")
location = input("Please enter your location: ")
year_birth = input("Please enter your year of birth: ")
details = firstname+" "+lastname+" "+location+" "+year_birth
print(details)
print("firstname {} lastname {} location {} year_birth{}".format(firstname, lastname, location, year_birth))