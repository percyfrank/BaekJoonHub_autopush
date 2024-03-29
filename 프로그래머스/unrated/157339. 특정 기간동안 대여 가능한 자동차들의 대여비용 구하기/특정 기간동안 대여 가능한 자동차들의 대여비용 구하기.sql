SELECT DISTINCT C.CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * (100-P.DISCOUNT_RATE) / 100 * 30) AS 'FEE'
FROM CAR_RENTAL_COMPANY_CAR C  JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H 
ON C.CAR_ID = H.CAR_ID 
 JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_TYPE IN ('세단','SUV')
AND C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
    )
AND P.DURATION_TYPE = '30일 이상'
AND ROUND(C.DAILY_FEE * (100-P.DISCOUNT_RATE) / 100 * 30) BETWEEN 500000 AND 2000000
ORDER BY ROUND(C.DAILY_FEE * (100-P.DISCOUNT_RATE) / 100 * 30) DESC, C.CAR_TYPE ASC, C.CAR_ID DESC