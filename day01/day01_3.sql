ALTER TABLE `scores`.`scores` 
ADD INDEX `fk_exam_idx` (`exam_id` ASC) VISIBLE;
;
ALTER TABLE `scores`.`scores` 
ADD CONSTRAINT `fk_exam`
  FOREIGN KEY (`exam_id`)
  REFERENCES `scores`.`exam_type` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;