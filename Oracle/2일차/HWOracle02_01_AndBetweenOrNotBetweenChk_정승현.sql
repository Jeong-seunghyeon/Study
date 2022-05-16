select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", DEPARTMENT_ID as "부서이름", JOB_ID as "직위"
 from EMPLOYEEs
where SALARY >= 2500 AND SALARY <= 3000
/

select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", DEPARTMENT_ID as "부서이름", JOB_ID as "직위"
 from EMPLOYEEs
where SALARY BETWEEN 2500 AND 3000
/

select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", DEPARTMENT_ID as "부서이름", JOB_ID as "직위"
 from EMPLOYEEs
where SALARY >= 2500 or SALARY <= 3000
/

select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", DEPARTMENT_ID as "부서이름", JOB_ID as "직위"
 from EMPLOYEEs
where SALARY NOT BETWEEN 2500 AND 3000
/
