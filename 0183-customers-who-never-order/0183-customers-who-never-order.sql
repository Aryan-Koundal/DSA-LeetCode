# Write your MySQL query statement below
select name as Customers from Customers left join Orders as c on Customers.id = c.customerId where c.customerId is null;