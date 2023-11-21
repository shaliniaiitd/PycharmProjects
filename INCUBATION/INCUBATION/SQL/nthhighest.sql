select * from (select salary from employee order by desc ) where rownum <= n

select salary from employee order by salary desc  limit 1 offset n-1