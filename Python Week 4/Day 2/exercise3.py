# ask the user for the number of students
# for each student, ask for their name, registration number,name of the school
# for each student, ask for the number of subjects they'd like to enter
# for each subject, record the marks
# output the student details:
# - name of student
# - school name
# - subject and mark

num=int(input("What is the number of students? "))
students=[]
for student in range(num):
    name=input("What is the student's name? ")
    #reg=input("What is their registration number? ")
    #school=input("What is the name of their school ")
    
    sub=int(input("How many subjects would they like to enter? "))
    subjects=[]
    for each_subject in range (sub):
        subject_name=(input("Please insert the name of the subject:"))
        subjects.append(subject_name)
        
for student in students:
    print(student)
    for subject in subjects:
        print(subject)
