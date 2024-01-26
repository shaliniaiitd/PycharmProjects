select emp_id,salary,
RANK() OVER(order by salary desc) as rnk,
dense_rank() OVER(order by salary desc) as dense_rnk
from employee

create table login_details(
login_id int primary key,
user_name varchar(50) not null,
login_date date);

From the login_details table, fetch the users who logged in consecutively 3 or more times.