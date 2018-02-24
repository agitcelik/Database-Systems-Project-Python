
#1NF I make department attribute of Student entity  divide into a new table which has dept_id and dept_name below because int and string both
#have same area
# CREATE TABLE `Student` (student_id INT NOT NULL, department varchar(255), reg_type varchar(255), reg_date DATETIME, PRIMARY KEY (`student_id`) );
#Student entity also violates 3NF 
use cmpe351;



CREATE TABLE Department (department_id INT, department_name varchar(255), PRIMARY KEY(department_id));

INSERT INTO Department VALUES (200,"Computer Engineering");
INSERT INTO Department VALUES (201,"Genetics and Bioengineering");
INSERT INTO Department VALUES (203,"Industrial Engineering");
#then, SET department 

# CREATE TABLE `Student` (student_id INT NOT NULL, department varchar(255), reg_type varchar(255), reg_date DATETIME, PRIMARY KEY (`student_id`) );
UPDATE Student SET department = 201 WHERE department = "201.Genetics and Bioengineering";
UPDATE Student SET department = 200 WHERE department = "200.Computer Engineering";
UPDATE Student SET department = 203 WHERE department = "203.Industrial Engineering";



# CREATE TABLE `Submission` (`assignment_id` INT NOT NULL,`student_id` INT NOT NULL,`grade` INT ,`deadline` DATE,`sub_date` DATE,
# PRIMARY KEY (`assignment_id`, `student_id`), CONSTRAINT fk_student FOREIGN KEY(student_id)REFERENCES student(student_id));


ALTER TABLE Submission DROP COLUMN deadline;
#2NF I create new Assigment table, because while assigment_id defines deadline attribute, student_id defines sub_date and grade attributes
#and bonus are defined by both student_id and assigment_id

CREATE TABLE Assignment (assignment_id INT, deadline DATETIME, PRIMARY KEY(assignment_id));

INSERT INTO Assignment VALUES(10,'2017-10-12 00:00:00');
INSERT INTO Assignment VALUES(11,'2017-10-12 00:00:00');
INSERT INTO Assignment VALUES(12,'2017-10-12 00:00:00');

