select DISTINCT Customer.CustomerId, Customer.FirstName, Customer.Phone, Customer.Company, Customer.City, Customer.Email from Customer
INNER join Employee on Customer.SupportRepId=(SELECT Employee.EmployeeId FROM Employee WHERE BirthDate>= DATE('now', '-50 years'))
INNER JOIN Invoice on Customer.CustomerId=Invoice.CustomerId
INNER JOIN InvoiceLine on Invoice.InvoiceId=InvoiceLine.InvoiceId
INNER JOIN Track on InvoiceLine.TrackId=Track.TrackId
INNER JOIN Genre on Track.GenreId=(SELECT Genre.GenreId FROM Genre WHERE Genre.Name NOT in ('Rock'))
ORDER by Customer.City ASC, Customer.Email DESC LIMIT 10
