create table gogek(
gobun number(3) PRIMARY KEY,
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3),
FOREIGN KEY (godam) REFERENCES sawon(sabun)
)
/