-- scores 데이터 베이스 사용
use scores;

-- table 내용 조회 : students테이블에서 name, grade, class 필드 불러오기
-- students 테이블 s로 별칭 지정
select s.name, s.grade, s.class
from students s;

-- CRUD 
-- create(insert), read(select), update(update), delete(delete)

insert into students(name, grade, class) 
values("송지효", 5, 2);

insert into students(name, grade, class) 
values("지석진", 4, 3);

insert into students(name, grade, class) 
values("양세찬", 4, 3);

-- 레코드의 갯수 반환, count(*)을 as를 이용하여 count로 필드명 바꿈
select count(*) as count from students;

-- 6학년 학생 불러옴
select s.name, s.grade, s.class
from students s
where grade = 6;

-- 이름이 김으로 시작하는 학생 불러옴
select s.name, s.grade, s.class
from students s
where name like "김%";

-- 6학년 학생들을 name 필드 기준으로 역순 정렬
select s.name, s.grade, s.class
from students s
where grade > 5
order by name desc;

-- student_id가 1인 학생 불러옴
select *
from scores
where student_id = 1;

-- students테이블의 id와 scores테이블의 student_id가 같은 students테이블의 학생 출력 
select students.name,
scores.kor, scores.eng, scores.math
from students, scores
where students.id = scores.student_id;

insert into scores(student_id, kor, eng, math, exam_id)
values(4,90,90,80,1);

-- 조인하기
select students.name,
scores.kor, scores.eng, scores.math, exam_type.exam_name
from scores
inner join students on scores.student_id = students.id
inner join exam_type on scores.exam_id = exam_type.id;

create view students_score as
select students.name,
scores.kor, scores.eng, scores.math, exam_type.exam_name
from scores
inner join students on scores.student_id = students.id
inner join exam_type on scores.exam_id = exam_type.id;

select * from students_score;