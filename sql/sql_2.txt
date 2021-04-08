select e.FirstName, e.LastName, e.Phone, er.FirstName, er.LastName, er.Phone
from Employee as e
inner join Employee as er on er.EmployeeId = e.ReportsTo