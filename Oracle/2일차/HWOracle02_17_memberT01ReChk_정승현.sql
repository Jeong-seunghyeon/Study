drop table memberT01;
purge recyclebin;

create table memberT01(
mem_name varchar2(20),
mem_id varchar2(20),
mem_pwd varchar2(20),
mem_email varchar2(30),
mem_phone varchar2(20),
mem_addr varchar2(30)
);

select*
from tab;

desc MEMBERT01;