--Write a SQL query to fetch the second last record from a employee table.

select * from (select *, row_num as r from employee order by employee_id desc) x where x.r = 2

select * from employee order by employee_id desc  limit 1 offset 1
