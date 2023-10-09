SELECT TOP 10
    Date,
    SUM(All Commodity Price Index) AS total_price_index
FROM Commodity Price Index
GROUP BY Date
ORDER BY total_price_index DESC

