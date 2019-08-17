# Database-Systems-Project-Python
,Introduction;
	I imported pymysql and install it to my computer; therefore, it should be installed in computer which that projet will be tested.
	by using either that syntax 'pip install pymysql' or 'conda install pymysql'.
			pymysql library allows me connect MYSQL and manipulate databases by using python

	also, I imported pandas librar to read .csv file , it should be installed in computer which that projet will be tested.
	by using either that syntax 'pip install pandas' or 'conda install pandas'.

	and imported datatime and random libraries in order to assign dates of databases randomly.

Then, 

studentData = panda.read_csv("C:/Users/HP/Desktop/Project/student_thurs.csv", sep=";")
							"This part should be changed with respect to directory of .csv file"
							       because, it may not read .csv due to wrong directory

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                            ...............) 
    user and password should be fixed with respect to computer that this project want to compile


After that, at first drop database statement must be removed, since there is no database named "cmpe351"


	




Part1;
	I design database by using online tool called LucidChart and
	there is a screenshot (named '.jpeg') of ER diagrams and I showed partial and total relationships between Entities

Part2;
	I use export feature of LucidChart instead of writing each query from scratch.
	by using cursor.execute("QUERIES") I insert them into my database

	for index, row in studentData.iterrows():
	  I  iterated over studentData to insert tuples to the Student table

	then create random student grades midterm,quiz,lab_grade and insert them into a tuple
	after that again insert them by using for loop to the course_grade,

	I create generateDate() method to insert them into subgrade,subDate columns

Part3
	I added quiz attribute

	Calculate overall by using  overOfAllGrades(mid,quiz,lab,final): method 

	then add bonus attribute which has default value 10

	and sort them by their midterm grades

Part4
	I create normalization.sql and made comment on that .sql file



then open cmd and write mysql -u root -p
						then type password

then 
write

>>python directory

after that

>>Select * from student;

>>Select * from submission;

>>Select * from course_grade;

for normalization

>>source   ....../normalization.sql

>>select * from Department;

>>select * from Assignment;

>>select * from Submission;

to show normalization changes....
