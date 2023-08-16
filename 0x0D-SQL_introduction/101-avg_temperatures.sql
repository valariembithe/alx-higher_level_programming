-- script that displays the average temperature (F) by city ordered by temp
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
