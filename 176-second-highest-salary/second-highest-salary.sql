# Write your MySQL query statement below
#approach 1
select max(salary) as SecondHighestSalary
from  Employee
where salary < (
    select max(salary) 
    from Employee
)
