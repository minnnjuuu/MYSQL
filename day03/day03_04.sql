use scores;

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