# Write your MySQL query statement below
select e.name as Employee from Employee as e join Employee as manager ON e.managerId = manager.id where e.salary > manager.salary;