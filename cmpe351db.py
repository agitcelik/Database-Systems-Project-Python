#This script connects to mysql server with given connection parameters. 
#Modify the user, password and database information to adapt to your environment. 
#Before running, make sure that you activated the cmpe351 virtual environment and installed pymysql within the environment. 

import pymysql.cursors #import cursors module of pymysql package
import pandas as panda
import random
from datetime import date
from datetime import datetime

def generateDate():
    birth_date = datetime(2017, random.choice(range(1, 13)), random.choice(range(1, 29))
        ,random.choice(range(1,24)),random.choice(range(0,59)),random.choice(range(0,59)))
    return birth_date

def overOfAllGrades(mid,quiz,lab,final):
    return (mid*25+quiz*15+lab*20+final*40)/100

deadline1 = generateDate()
deadline2 = generateDate()
deadline3 = generateDate()

assignment_idList= [10,11,12]


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             charset = 'utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#part2.b reading csv by using pandas
studentData = panda.read_csv("C:/Users/HP/Desktop/Project/student_thurs.csv", sep=";")

try:
    with connection.cursor() as cursor:
        mysqlQuery = """drop database cmpe351"""
        cursor.execute(mysqlQuery)
        #part2.a
        mysqlQuery = """CREATE DATABASE IF NOT EXISTS cmpe351"""
        cursor.execute(mysqlQuery)


        mysqlQuery = """use cmpe351"""
        cursor.execute(mysqlQuery)



        mysqlQuery = """CREATE TABLE `Student` (
                    student_id INT NOT NULL,
                    department varchar(255),
                    reg_type varchar(255),
                    reg_date DATETIME,
                    PRIMARY KEY (`student_id`));    """
        cursor.execute(mysqlQuery)


        mysqlQuery = """CREATE TABLE `Submission` (
                    `assignment_id` INT NOT NULL,
                    `student_id` INT NOT NULL,
                    `grade` INT ,
                    `deadline` DATETIME,
                    `sub_date` DATETIME,
                    PRIMARY KEY (`assignment_id`, `student_id`),
                    CONSTRAINT fk_student FOREIGN KEY(student_id)
                    REFERENCES student(student_id)
                    );    """
        cursor.execute(mysqlQuery)



        mysqlQuery = """CREATE TABLE `Course_grade` (
                    `student_id` INT,
                    `midertm` INT,
                    `final` INT,
                    `lab_grade` INT,
                     CONSTRAINT fk_grade_student FOREIGN KEY(student_id)
                     REFERENCES student(student_id)
                   );  """
        cursor.execute(mysqlQuery)

        studentIDList =[]
        #part2.c insert datas from student_thurs.csv to the created cmpe351 databases     
        for index, row in studentData.iterrows():

            studentIDList.append(row['StudentID'])
            insertQuery =f""" INSERT INTO student VALUES ({row['StudentID']}, '{ row['Department']}', '{row ['Reg. Type']}', "{row ['Reg. Date']}")"""#.format(id=eachStud_ID, dep=department, date=reg_date, type=reg_type)

            cursor.execute(insertQuery)

        

        #part3.a
        alterQuizTable = """ALTER TABLE Course_grade ADD quiz INT """
        cursor.execute(alterQuizTable)
        for eachStud_ID in studentIDList:
            midtermRandom=random.randrange(100)
            finalRandom=random.randrange(100)
            labRandom=random.randrange(100)
            quizRandom=random.randrange(100)
            #part2.d
            gradeTuple = (midtermRandom, finalRandom,labRandom,quizRandom)
            
            
            insertQuery2 =f""" INSERT INTO Course_grade VALUES ({eachStud_ID}, {gradeTuple[0]}, {gradeTuple[1]}, {gradeTuple[2]},{gradeTuple[3]})"""
            #part3.b

            print('Overall of ',eachStud_ID,' is:',overOfAllGrades(gradeTuple[0],gradeTuple[3],gradeTuple[2],gradeTuple[1]))
            cursor.execute(insertQuery2)

        showCourse_grade = """ SELECT * FROM Course_grade"""
        cursor.execute(showCourse_grade)    
        result = cursor.fetchall()

        print("Course_grade TABLE w/ quiz attribute")
        for row in result:
            print(row)

        connection.commit() 



        
        for eachStud_ID in studentIDList:
            
            randomAssigmentGrade=random.randrange(100)
            tuple=(assignment_idList[0],randomAssigmentGrade)
            randomSubDate= generateDate()
         
            
            insertQuery3 =f""" INSERT INTO Submission VALUES ({tuple[0]},{eachStud_ID},{tuple[1]},'{deadline1}','{randomSubDate}')"""#.format(assignment_id=tuple[0], student_id=eachStud_ID, grade=tuple[1], deadline=date1, sub_date=subDate)

            cursor.execute(insertQuery3)


        connection.commit() 

        for eachStud_ID in studentIDList:
            randomAssigmentGrade=random.randrange(100)
            tuple=(assignment_idList[1],randomAssigmentGrade)
            randomSubDate= generateDate()

            insertQuery3 =f""" INSERT INTO Submission VALUES ({tuple[0]}, {eachStud_ID}, {tuple[1]}, '{deadline2}', '{randomSubDate}')"""

            cursor.execute(insertQuery3)
        

        connection.commit()      
        for eachStud_ID in studentIDList:
            randomAssigmentGrade=random.randrange(100)
            tuple=(assignment_idList[2],randomAssigmentGrade)
            randomSubDate= generateDate()

            insertQuery3 =f""" INSERT INTO Submission VALUES ({tuple[0]}, {eachStud_ID}, {tuple[1]}, '{deadline3}', '{randomSubDate}')"""
            #print(insertQuery3)

            cursor.execute(insertQuery3)



        #Part3.c     
        alterBonusTable = """ALTER TABLE Submission ADD COLUMN bonus INT DEFAULT 10 """
        cursor.execute(alterBonusTable)

        
        alterCompareDateTable = """ UPDATE Submission SET grade = bonus + grade WHERE deadline > sub_date """
        cursor.execute(alterCompareDateTable)
        
        #part3.d
        print(" View students with their course grades (midterm-ﬁnal-lab)")
        showCourse_grade = """ SELECT student_id, midertm, final, lab_grade FROM Course_grade"""
        cursor.execute(showCourse_grade)

        for row in cursor.fetchall():
            print(row)


        #Part3.e
        print(" Sort student with respect to their midterm grades")
        sortMidtermGrades = """ SELECT * FROM Course_grade ORDER BY midertm """
        cursor.execute(sortMidtermGrades) 

        for row in cursor.fetchall():
           print(row)

        

        connection.commit()


finally:
    connection.close()