SELECT FOOD_TYPE, REST_ID,REST_NAME, FAVORITES
FROM REST_INFO
WHERE FOOD_TYPE IN (SELECT FOOD_TYPE
                    FROM REST_INFO
                    GROUP BY FOOD_TYPE
                    HAVING FAVORITES = MAX(FAVORITES)
                   )
ORDER BY FOOD_TYPE DESC;