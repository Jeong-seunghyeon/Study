CREATE TABLE customer(
id VARCHAR2(20) NOT NULL,
pwd varchar2(20) NOT NULL,
name varchar2(20) not null,
phone varchar2(30),
address varchar2(100)
);


select OWNER, CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME
from user_cons_columns
/