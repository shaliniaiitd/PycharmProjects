select e.emp_id from employee e
inner join
(select department_name, Avg(salary) as avg_salary from employee group by department_name) viewSalary
on e.department_name = viewSalary.department_name
where e.salary > viewSalary.avg_salary
