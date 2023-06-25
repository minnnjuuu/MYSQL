-- employee database 생성
-- 사원, 부서, 직급 3개의 테이블 만들기
-- 사원 테이블에는 id, 이름, 부서코드(부서테이블의 id), 직급코드(직급테이블의 id), 외 기타 사원 정보
-- 부서 테이블에는 id, 부서명, 외 기타 부서 정보
-- 직급 테이블에는 id, 직급명, 외 기타 직급 정보
create database employee;

use employee;

create table staff(
id int primary key not null auto_increment,
name varchar(50) not null,
group_id int not null unique,
rank_id int not null unique
-- foreign key(id) references staff_group(staff_group_id),
-- foreign key(id) references staff_rank(staff_rank_id)
);

create table staff_group(
staff_group_id int primary key not null unique,
group_name varchar(50) not null
);


create table staff_rank(
staff_rank_id int primary key not null unique,
rank_name varchar(50) not null
);

show tables;

ALTER TABLE `employee`.`staff` 
ADD CONSTRAINT `fk_group_id`
  FOREIGN KEY (`group_id`)
  REFERENCES `employee`.`staff_group` (`staff_group_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `employee`.`staff` 
ADD CONSTRAINT `fk_rank_id`
  FOREIGN KEY (`rank_id`)
  REFERENCES `employee`.`staff_rank` (`staff_rank_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;