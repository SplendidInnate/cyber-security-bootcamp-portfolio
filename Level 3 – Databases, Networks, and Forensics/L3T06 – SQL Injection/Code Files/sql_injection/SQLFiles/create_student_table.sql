CREATE TABLE Student (
student_id CHAR(13) PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email varchar(30) NOT NULL,
address_id INTEGER NOT NULL,

FOREIGN KEY(address_id) REFERENCES Address(address_id));