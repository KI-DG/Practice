CREATE TABLE contacts(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);
-- 새로운 테이블을 만드는 것

ALTER TABLE contacts RENAME TO new_contacts;
-- 기존의 테이블 이름을 바꿔주는것 

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;
-- 기존의 컬럼의 이름을 바꿔주는것

ALTER TABLE new_contacts ADD COLUMN address Text NOT NULL;
-- 컬럼을 추가 되는 것
-- 주의사항 테이블에 데이터가 있는경우
-- Cannot add NOT NULL column with default value NULL (오류발생)
-- 해결방법
-- ALTER TABLE new_contacts ADD COLUMN address Text NOT NULL DEFAULT 'no address';

ALTER TABLE new_contacts DROP COLUMN address;
-- 컬럼 삭제
-- 삭제하지 못하는경우 
-- 컬럼이 다른 부분에서 참조되는 경우
-- PRIMARY KEY 인경우
-- UNIQUE 제약조건이 있는 경우

DROP TABLE new_contacts;
-- 테이블 삭제
-- 한 번에 하나의 테이블만 삭제 
-- 여러 테이블을 제거하려면 여러번 사용
-- 실행취소하거나 복구할 수 없음