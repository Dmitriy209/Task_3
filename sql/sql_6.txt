SELECT DISTINCT Genre.Name, Track.Name, Album.Title, Artist.Name FROM Track
INNER JOIN Genre on Track.GenreId=(SELECT Genre.GenreId WHERE Genre.Name=(SELECT Genre.Name FROM Track LEFT JOIN InvoiceLine on InvoiceLine.TrackId=Track.TrackId LEFT JOIN Genre on Genre.GenreId=Track.GenreId GROUP BY Genre.Name ORDER by count() DESC LIMIT 1))
INNER JOIN Album on Album.AlbumId=Track.AlbumId
INNER JOIN Artist on Artist.ArtistId=Album.ArtistId