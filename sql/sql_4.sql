SELECT DISTINCT Customer.FirstName || Customer.LastName as full_name, Customer.Phone, Customer.City FROM Customer
INNER JOIN Invoice on Invoice.CustomerId=Customer.CustomerId
WHERE City in (SELECT Customer.City FROM Customer GROUP BY City HAVING COUNT(City)>1)