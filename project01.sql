--   1-TASK

CREATE TABLE students(
id SERIAL PRIMARY KEY,
name VARCHAR(64) NOT NULL,
age INT NOT NULL,
group_name  VARCHAR(64)
);

CREATE TABLE grades(
id SERIAL PRIMARY KEY,
student_id INT REFERENCES students(id),
subject TEXT NOT NULL ,
grade INT NOT NULL
);


-- 2-TASK

INSERT INTO students(name, age, group_name)
VALUES 
('ALI', 21, 'ATT-201'),
('John',20, 'ATT-202'),
('Mira', 23, 'ATM-204'),
('Vali', 25, 'ATT-100'),
('Bob', 24, 'ATT-140');

INSERT INTO grades(student_id,subject, grade)
VALUES 
(1,'Algebra', 85),
(5,'Fizika', 95),
(2,'Chet tili', 80),
(3,'Rus tili', 75),
(4,'Fizika', 65);

-- 3-TASK

SELECT name, group_name FROM students;

-- 4-TASK

SELECT students.name,grades.grade FROM students JOIN grades ON students.id=grades.student_id;

-- 5-TASK

SELECT name, age FROM students WHERE age >20;

-- 6-TASK

SELECT AVG(grade) AS ortacha FROM grades;

-- 7-TASK

SELECT COUNT(*) AS soni FROM grades;

--  8-TASK

SELECT students.name, grades.grade FROM students JOIN grades ON students.id=grades.student_id ORDER BY grades.grade DESC LIMIT 1;

-- 9=TASK

SELECT * FROM students WHERE name LIKE 'A%' ;

-- 10_TASK

DELETE FROM students WHERE name = 'Group C';