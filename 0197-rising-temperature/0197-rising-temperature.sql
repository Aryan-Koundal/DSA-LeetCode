SELECT id
FROM (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS previous_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS previous_date
    FROM Weather
) AS w
WHERE temperature > previous_temp and 
recordDate = DATE_ADD(previous_date, INTERVAL 1 DAY);