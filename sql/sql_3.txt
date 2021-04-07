select DISTINCT Customer.FirstName, Customer.Phone FROM Customer
INNER JOIN Invoice on Customer.CustomerId=Invoice.CustomerId
INNER JOIN InvoiceLine on Invoice.InvoiceId=(SELECT InvoiceLine.InvoiceId FROM Invoice where UnitPrice=(SELECT max(UnitPrice) FROM Track))
ORDER by FirstName
