-- retrievemax  temperature
SELECT state, MAX(temp) AS max_temp
FROM Temperatures
GROUP BY state
ORDER BY state;
