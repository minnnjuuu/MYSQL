use scores;
show tables;

create table exam_type(
id int primary key not null auto_increment unique,
exam_name varchar(50) not null,
exam_date timestamp not null
);

show tables;

-- table 객체를 수정함
alter table scores
add constraint fk_student
foreign key (student_id) references students(id);

-- student table에 레코드를 삽입
insert into students(name, grade, class)
values("유재석",6,1);

insert into students(name, grade, class)
values("강호동",6,1);

insert into students(name, grade, class)
values("김종국",6,1);

-- student table의 내용 확인
select * from students;

insert into exam_type(exam_name, exam_date)
values("2023학년도 1학기 중간고사","2023-06-01");

select * from exam_type;

insert into scores(student_id,kor,eng,math,exam_id)
values(1,90,75,80,1);

insert into scores(student_id,kor,eng,math,exam_id)
values(2,95,70,70,1);

insert into scores(student_id,kor,eng,math,exam_id)
values(3,75,85,90,1);

select * from scores;