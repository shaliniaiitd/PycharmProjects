select emp_id,salary,
RANK() OVER(order by salary desc) as rnk,
dense_rank() OVER(order by salary desc) as dense_rnk
from employee