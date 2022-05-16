create table sawon(
sabun number(3) PRIMARY KEY,
saname varchar2(10) NOT NULL,
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date DEFAULT sysdate,
sasex varchar2(6),
samgr number(3),
FOREIGN KEY (deptno) REFERENCES dept(deptno),
FOREIGN KEY (samgr) REFERENCES sawon(sabun),
CONSTRAINT sawon_sasex_ck CHECK (sasex='남자' or sasex='여자')
)
/