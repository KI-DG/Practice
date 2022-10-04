CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age
FROM users;
-- 필요한거만 불러온다
SELECT * FROM users;
-- 전체 데이터 조회
SELECT rowid, first_name
FROM users;
-- rowid 조회하는법

SELECT first_name, age FROM users
ORDER BY age ASC;
-- 오름차순

SELECT first_name, age FROM users
ORDER BY age DESC;
-- 나이 많은 순

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;
-- 정렬의 방향을 두개 해줄수 있다
-- 정렬할때 NULL은 가장 작은 값

SELECT country FROM users;
-- 지역 전체 조회
SELECT DISTINCT country FROM users;
-- 중복 없이 조회
SELECT DISTINCT country FROM users ORDER BY country;
-- 지역순으로 중복없이 내림차순 조회
SELECT DISTINCT first_name, country FROM users ASC;
-- 이름과 지역을 중복없이 조회
SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;
-- 이름과 지역 중복 없이 지역순으로 내림차순 정렬하여 모든 이름과 조회하기

SELECT first_name, age, balance FROM users
WHERE age >= 30;
-- 나이가 30살 이상인 이름, 나이, 계좌 조회
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;
-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 조회

SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';
-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회

SELECT first_name FROM users
WHERE first_name LIKE '%준';
-- 이름이 '준'으로 끝나는 사람들의 이름 조회

SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';
-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회

SELECT first_name, age FROM users
WHERE age LIKE '2_';
-- 나이가 20대인 사람들의 이름과 니이 조회


SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__%';
-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회

SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');
-- ==
-- SELECT first_name, country FROM users
-- WHERE country= '경기도' OR country = '강원도';
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역조회

SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');
-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회

SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;
-- 나이가 20살이상 30살 이하인 사람들

SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;
-- 나이가 20살이상 30살 이하가 아닌 사람들

SELECT rowid, first_name FROM users 
LIMIT 10;
-- 첫번째부터 열번째 데이터까지

SELECT first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;
-- 계좌 잔고가 가장 많은 10명의 이름과 계좌잔고

SELECT first_name, age FROM users
ORDER BY age ASC LIMIT 5;
-- 나이가 가장 어린 5명의 이름과 나이 조회하기

SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

SELECT country, COUNT(*) FROM users GROUP BY country;
-- 각 지역별로 몇명씩 살고 있는지 조회

