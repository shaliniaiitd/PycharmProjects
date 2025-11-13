#1. Write a query to return employee record with highest salary

select * from employee where salary = select Max(salary) from employee

/* 2. Return the second highest salary from employee table */

select max(salary) from employee where salary Not In select max(salary) from employee

/* 3. Select range of employee based on id

select * from employee where employee_id between min and max

/*5. return an employee with the highest salary and the employee's  department_name*/
select e.emp_id,e.salary, d.name from employee e inner join departmenet d on e.dept_id = department.id where e.salary = (select max(salary) from employee)  


/*6. Return highest salary, employee_name, department_name for each department*/
select e.name, d.name from employee e inner join department d on e.dept_id = d.id where (e.dept_id,e.salary) in (select dept_id,max(salary) from employee group by dept_id)

/*7 select DISTINCT name as new_column from employee

/*8 Fetch all duplicate records in a table

select <unique_col>, count(*) as duplicate_count from employee group by (<unique col> having count(*) >1 

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
select name, hire_date from employee where MONTH(hire_date) = 12 

/*20 names starting with J and ends with S
where name like 'J%S'

/*21 Display nth row in a table. Rownum does not work with = and >; can only use < and = operators.Rownum works only in OLD ORACLE.

select * from (select employee.*, rownum rn from employee) where rn = n
/* FOR SQL SERVER/MYSQL, use window function ROW_NUMBER instead
select * from (select *,ROW_NUMBER OVER(ORDER BY salary Desc) from employee) as rn where rn =3


#UNION all INCLUDES DUPLICATES

#INNER JOINS - there must be matching row in right table for the row in left table
Table1 Table2
1       1
1       1
1       2
2       2
4       5
How many rows would result from following:
INNER JOIN - 1X2 + 1X2 + 1X2 + 1X2  = 8
LEFT JOIN (1 left join2) = 6 + 1X2 +1 = 9
RIGHT JOIN(1 right join 2) = 2X3 + 2X1 + 1 = 9
OUTER (FULL) JOIN = 8+2 = 10
CROSS JOIN = 5X5 = 25


/*22  Display employees who are working in location Chicago from emp and dept table
select names from employee e
inner join department d on e.department_id = d.department_id where d.location = 'Chicago'


/*23 Display the department name and total salaries from each department
select d.department_name, sum(e.salary) from employee e
inner join department d
on e.department_id = d.department_id
 group by department_name

#SELF JOIN

/*24 Display employee details who are getting more salary than their manager salary*/

select e1.* from employee e1, employee e2 where e1.MGR = e2.id and e1.salary>e2.salary

/*25 Display the employee details who joined before their manager */
select e1.* from  employee e1, employee e2 where e1.mgr = e2.id and e1.join_date < e2.join_date


#LEFT JOIN - All rows from left table and matching rows from right table are displayed

#CROSS JOIN


/*26 m rows of table are crossed with n rows of table 2 to give total mxn rows. */

#DISPLAY FIRST n rows or last n rows

/*27 Display first and last row of a table
select * from (select emp.*,rownum rn from emp ) where rn = 1 or rn = select count(*) from employee

/*28 Display last 2 rows of a table

select * from (select emp.*,rownum rn from emp ) where rn > (select count(*) -2 from emp)
/*29 Display first and last 2 rows of the table
select * from (select emp.*,rownum rn from emp ) where rn in(1,2) or rn > (select count(*) -2 from emp)

#Nth HIGHEST record

/*30 Display nth highest salary


select * from (select distinct salary,rownum  from emp order by salary desc) where rownum = n
/* USING ROW_NUMBER = nth highest salary
select * from (select salary,ROW_NUMBER() OVER(Order by salary desc) as RN from employee) where RN =n

/* RANK employee salaries

select salary, RANK() OVER(order by salary desc) as salary_rank from employee 

/* DENSE_RANK - doesnt skip rank in case of a tie
select salary, DENSE_RANK() OVER(order by salary desc) as salary_rank from employee 

/*PARTITION BY - used in place of group by inside OVER() to aggregate over a column. Does not summarise the rows(like group by) but displays the aggregate value as additional column with all rows. 
select salary, RANK() OVER(PARTITION BY department_id order by salary desc) as salary_rank from employee - gives department wise salary ranks






