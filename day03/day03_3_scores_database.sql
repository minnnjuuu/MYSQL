use scores;

create view select_all_from_scores as
select students.name,
scores.kor,
scores.eng,
scores.math,
scores.total,
scores.avgs,
exam_type.exam_name
from scores.scores
inner join students on students.id = scores.student_id
inner join exam_type on exam_type.id = scores.exam_id;

select * from select_all_from_scores;
-- view는 읽기용으로만 사용

delimiter $$
create procedure calc_total_avg()
begin
	update scores 
    set total = kor + eng + math,
    avgs = (kor + eng + math)/3 where total is null;
end $$
delimiter ; -- delimiter 쓰고 한 칸 띄우기

call calc_total_avg();