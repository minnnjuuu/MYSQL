CREATE TABLE `scores`.`scores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `kor` INT NOT NULL,
  `eng` INT NOT NULL,
  `math` INT NOT NULL,
  `total` INT NULL,
  `avgs` FLOAT NULL,
  `exam_id` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_as_ci
COMMENT = '시험 성적 테이블';
