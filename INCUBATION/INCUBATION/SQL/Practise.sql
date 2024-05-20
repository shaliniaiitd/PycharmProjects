#1. Write a query to return employee record with highest salary

select * from employee where salary = select Max(salary) from employee

/* 2. Return the second highest salary from employee table */

select max(salary) from employee where salary Not In select max(salary) from employee

/* 3. Select range of employee based on id

select * from employee where employee_id between min and max

/*5. return an employee with the highest salary and the employee's  department_name*/

select e.employee_name, d.department_name
from employee e
inner join department  d
on e.department_id = d.department_id
where e.salary IN select max(salary) from employee

/*6. Return highest salary, employee_name, department_name for each department*/

select e.salary, e.employee_name,d.department_name from employee e
inner join department d
 on e.department_id = d.department_id
 where e.salary IN (select MAX(salary) from employee  group by department_id)

/*7 select DISTINCT name as new_column from employee

/*8 Fetch all duplicate records in a table

select * from employee where name NOT In (select DISTINCT name from employee)

/*9 display department-wsie highest salary

select Max(salary), department_id from employee group by department_id

/*10 Display alternate records
select * from (select name,salary, rownum rn from employee order by rn) where mod(rn,2) == 0

/*11 Display duplicate of a column
select column_name, count(column_name)  from table
group by column_name
having count(column_name)>1
order by count(column_name) desc

#PATTERN MATCHING
/* 12 Display employee names whose name start with 'M'*/

select name from employee where name like 'M%'

/*13 Display names of all employees having "M" in any position in their name
select name from employee where name like "%M%"

/*14 Display the names of all employees whose name does not contain 'M' anywhere
select name from employee where name not like "%M%"

/* 15 Display employee names whose name ends with 'M'*/
select name from employee where name like '%M'

/* 16. Display names of all employees whose name contains exactly 4 letters

select names from employee where name like '____'

/*17 Display names of employees whose name contains the (i) second letter as 'L' (ii) fourth letter as 'M'
select names from employee where name like '_L__'
select names from employee where name like '___M'

/*18 Display names whose name contains 2 L's'
select names from employee where name like '%L%l%'

/*19 names and hire dates for the employees joined in the month of December
select name, hire_date from employee where hire_date like "%DEC%"

/*20 names starting with J and ends with S
where name like 'J%S'

/*21 Display nth row in a table. Rownum does not work with = and >; can only use < and = operators.

select * from (select employee.*, rowcount rn from employee) where rn = n

#UNION all INCLUDES DUPLICATES

#INNER JOINS - there must be matching row in right table for the row in left table
/*22  Display employees who are working in location Chicago from emp and dept table

select names from employee e
inner join department d on e.department_id = d.department_id where d.department_name = 'Chicago'


/*23 Display the department name and total salaries from each department
select d.department_name, sum(e.salary) from employee e
inner join department d
where e.department_id = d.department_id
 group by department_name

#SELF JOIN

/*24 Display employee details who are getting more salary than their manager salary*/

select e1.* from employee e1, employee e2 where e1.MGR = e2.id and e1.salary>e2.salary

/*25 Display the employee details who joined before their manager */

select e1.* from employee e1, employee e2 where e1.MGR = e2.id and e1.hire_date >e2.hire_date

#LEFT JOIN - All rows from left table and matching rows from right table are displayed

#CROSS JOIN


/*26 m rows of table are crossed with n rows of table 2 to give total mxn rows. */

#DISPLAY FIRST n rows or last n rows

/*27 Display first and last row of a table
select * from (select emp.*,rownum rn from emp ) where rn = 1 or r = (select count(*) from emp)

/*28 Display last 2 rows of a table
select * from (select emp.*,rownum rn from emp ) where rn > (select count(*) -2 from emp)
/*29 Display first and last 2 rows of the table
select * from (select emp.*,rownum rn from emp ) where rn in(1,2) or rn > (select count(*) -2 from emp)

#Nth HIGHEST record

/*30 Display nth highest salary
#Get highest salary

select * from (select distinct salary from emp order by salary desc) where rownum <= n
minus
select * from (select distinct salary from emp order by salary desc) where rownum <= n-1




