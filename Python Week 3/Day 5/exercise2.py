# create a function that takes in the name of an employee, their salary and years of service
# calculate the bonus based on the years of service:
# if years of service <= 1: 10 %
# if years of service >1 and <= 2: 20 %
# if years of service >2 and <= 3: 30 %
# if years of service >3 and <= 4: 40 %
# if years of service >4 and <= 5: 50 %
# if years of service > 5: 60 %
# print the output as follows:
# "Hi Ben, for your 5 years of service, you get 10000 as bonus"

# name=input("Please insert your name here: ")
# salary= int(input("Please insert your current salary here: "))
# year=int(input("Please insert the year you started working here: "))
# years=2020-year
# def details(name, salary, years):
#     if years<=1:
#         bonus = 0.1* salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")

#     elif years>1 and years<= 2:
#         bonus = 0.2*salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")

#     elif years>2 and years<= 3:
#         bonus = 0.3*salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")

#     elif years>3 and years<= 4:
#         bonus = 0.4*salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")

#     elif years> 4 and years<= 5:
#         bonus = 0.5*salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")
#     elif years > 5:
#         bonus= 0.6*salary
#         print(f"Hi {name}, for your {years} years of service, you get {bonus} as bonus")

# details(name,salary,years)

import datetime

today = datetime.date
print(today)