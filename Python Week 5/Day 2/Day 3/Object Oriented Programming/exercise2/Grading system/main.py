from student import Student
from subject import Subject
from school import School
from grading import grading

student_number=int(input("How many students are we recording? "))
students = []

for index in range(1,student_number+1):
    
        name = input("Please input the student's name: ")
        stream = input("Please input their class and stream: ")
        
        school_name =  input("Please input the school name: ")
        school_address =  input("Please input the school address: ")

        school = School(school_name,school_address)   

        subject_number=int(input("How many subjects does the student take? "))
        subjects = []
        for subj in range(1,subject_number+1):
    
            subject_name=input("Please insert the subject name: ")
            score=int(input("Please insert the score: "))

            subject = Subject(subject_name,score)
            subjects.append(subject)

        student = Student(name,stream,school,subjects)
        students.append(student)


for student in students:
    print(f'\n NAME: {student.name} STREAM: {student.stream} SCHOOL: {student.school.name} NUMBER OF SUBJECTS: {len(student.subjects)}')
    for subject in subjects:
        print(f'\nSubject Name :{subject.name} Score : {subject.score} Grade: {grading(subject.score)}')




       

    