-- retrieve average temperature
SELECT city, AVG(temp) AS avg_temp
FROM Temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
