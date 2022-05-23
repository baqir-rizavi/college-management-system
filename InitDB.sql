DROP DATABASE IF EXISTS cms_db;

CREATE DATABASE IF NOT EXISTS cms_db;

USE cms_db;

CREATE TABLE IF NOT EXISTS users
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username varchar(100) unique not null,
  passwd varchar(100) not null,
  is_admin boolean not null
);

CREATE TABLE IF NOT EXISTS teacher
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name varchar(200) not null,
  salary int,
  experience FLOAT(6,3),
  no_of_courses int,
  usr_id int not null,
  foreign KEY (usr_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS student
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name varchar(200) not null,
  roll_no int,
  batch varchar(30),
  semester_dues int,
  current_semester int,
  usr_id int not null,
  foreign KEY (usr_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS course
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name varchar(40) unique not null,
  credit_hours int,
  teach_id int,
  foreign KEY (teach_id) REFERENCES teacher(id)
);

CREATE TABLE IF NOT EXISTS student_enrollment
(
  st_id int,
  cr_id int,
  enroll_date datetime,
  primary key (st_id, cr_id),
  foreign key (st_id) references student(id),
  foreign key (cr_id) references course(id)
);

CREATE TABLE IF NOT EXISTS attendance
(
  st_id int,
  cr_id int,
  on_day datetime,
  is_present varchar(1) check (is_present in('p','a')),
  primary key (st_id, cr_id, on_day),
  foreign key (st_id) references student(id),
  foreign key (cr_id) references course(id)
);

CREATE TABLE IF NOT EXISTS assignment
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  title varchar(100) not null,
  description varchar(1500),
  deadline datetime,
  cr_id int,
  foreign key (cr_id) references course(id)
);

CREATE TABLE IF NOT EXISTS assignment_status
(
  st_id int,
  ass_id int,
  is_complete boolean,
  primary key (st_id, ass_id),
  foreign key (st_id) references student(id),
  foreign key (ass_id) references assignment(id)
);

INSERT INTO users (username, passwd, is_admin)
VALUES ('admin', 'admin', true);