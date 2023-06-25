-- 할일 관리 데이터베이스 모델링 alter
-- 2개의 테이블이 필요함
--     회원 정보 테이블(id(자동증가),아이디(필수(notnull)), 비번(필수), 닉네임(필수),...)
--     할일 목록 테이블(id(자동증가), 할일, 만들어진 날짜, 완료날짜,user_id(외부키 회원정보테이블과 관계)...)
--

-- 할일 관리 데이터베이스 생성
create database to_do;

use to_do;

create table member_info(
id int primary key not null auto_increment,
member_id varchar(50) not null unique,
password varchar(50) not null,
member_name varchar(50) not null
);

create table to_do_list(
id int primary key not null auto_increment,
to_do varchar(50),
-- 기본값 NULL
write_date timestamp,
-- 기본값 현재시간
complete_date timestamp,
-- 완료 유무 기본값 false(0)
user_id varchar(50) not null unique
);

show tables;
describe member_info;
describe to_do_list;
