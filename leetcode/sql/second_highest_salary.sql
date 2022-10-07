-- https://leetcode.com/problems/second-highest-salary/



SELECT MAX(salary) as SecondHighestSalary
FROM Employee
WHERE salary not IN(SELECT MAX(salary)
                    FROM Employee)