# Write your MySQL query statement below
#approach 1
-- select max(salary) as SecondHighestSalary
-- from  Employee
-- where salary < (
--     select max(salary) 
--     from Employee
-- )

#approach 2 
-- select (
-- select distinct salary 
-- from Employee 
-- order by salary desc
-- limit 1 OFFSET 1 ) as SecondHighestSalary


#approach 3 
select (
    select distinct salary 
    from (
        select salary ,
        DENSE_RANK() over (order by salary desc) as rnk
        from Employee 
    ) t 
    where rnk = 2
) as SecondHighestSalary
