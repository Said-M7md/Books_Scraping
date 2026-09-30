-- Average price for each rating
SELECT	rating  as Rating,
		ROUND(AVG(price) , 2) as AVG_Price
FROM books
GROUP BY rating
ORDER BY rating;

-- The 5 most expensive books rated 4 or 5
SELECT TOP 5
       title,
       ROUND(price,2) price,
       rating
FROM dbo.books
WHERE rating >= 4
ORDER BY price DESC;

-- How many books are out of stock, per rating
SELECT rating,
       COUNT(*) AS out_of_stock_count
FROM books
WHERE in_stock = 'False'
GROUP BY rating
ORDER BY rating;