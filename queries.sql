CREATE DATABASE IF NOT EXISTS cmpe351;
use cmpe351

CREATE TABLE `Student` (
  student_id INT NOT NULL,
  department varchar(255),
  reg_type varchar(255),
  reg_date DATETIME,
  PRIMARY KEY (`student_id`)
);

CREATE TABLE `Course_grade` (
  `student_id` INT,
  `midertm` INT,
  `final` INT,
  `lab_grade` INT,
  CONSTRAINT fk_grade_student FOREIGN KEY(student_id)
  REFERENCES student(student_id)
 
);

CREATE TABLE `Submission` (
  `assignment_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `grade` INT ,
  `deadline` DATE,
  `sub_date` DATE,
  PRIMARY KEY (`assignment_id`, `student_id`),
  CONSTRAINT fk_student FOREIGN KEY(student_id)
  REFERENCES student(student_id)
 
);
