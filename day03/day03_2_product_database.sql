-- 상품(products) 데이터베이스 만들기
-- 카테고리 테이블 생성(id, 카테고리명, 외 기타등등)
-- 상품 테이블 (id, 상품명, 카테고리_id, 외 기타등등)

create database products;

use products;

create table category(
id int primary key not null auto_increment unique,
category_name varchar(50),
category_info varchar(500) 
);

create table product(
product_id int primary key not null auto_increment unique, 
product_name varchar(50),
price int not null,
product_info varchar(500) not null,
category_id int not null,
foreign key(category_id) references category(id)
);

create table product_image(
id int primary key not null auto_increment unique,
product_id int not null,
image_url varchar(500) not null,
foreign key(product_id) references product(product_id)
);

create table options(
id int primary key not null auto_increment unique,
option_name varchar(200) not null,
option_info varchar(500) not null,
product_id int not null,
foreign key(product_id) references product(product_id)
);

create table option_values(
id int primary key not null auto_increment unique,
option_name varchar(200) not null,
option_info varchar(200),
option_id int not null,
foreign key(option_id) references options(id)
);