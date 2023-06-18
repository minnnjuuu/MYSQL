-- 데이터 보여준다.
show databases;

-- 데이터베이스를 생성한다.
create database scores;

-- 지정된 데이터베이스를 사용한다.
use scores;

-- 데이터베이스에 있는 모든 테이블들을 보여준다.
show tables;

-- table : 데이터를 저장하고 관리하는 가장 기본적인 객체
create table students(
id int primary key not null auto_increment unique,
name varchar(50) not null,
grade int not null,
class int not null
);

show tables;
describe students;