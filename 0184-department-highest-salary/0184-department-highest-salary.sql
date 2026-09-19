SELECT Department, Employee, Salary FROM (
SELECT d.name AS Department,e.name AS Employee,e.salary AS Salary,RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS rank_num FROM Employee AS e JOIN Department AS d ON e.departmentId = d.id
) AS ranked WHERE rank_num = 1;