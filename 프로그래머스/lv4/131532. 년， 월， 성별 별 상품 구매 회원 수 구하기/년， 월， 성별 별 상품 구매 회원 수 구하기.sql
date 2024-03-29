SELECT YEAR(SALE.SALES_DATE) AS YEAR, 
       MONTH(SALE.SALES_DATE) AS MONTH,
       USER.GENDER,
       COUNT(DISTINCT USER.USER_ID) AS USERS
FROM USER_INFO USER JOIN ONLINE_SALE SALE
ON USER.USER_ID = SALE.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3