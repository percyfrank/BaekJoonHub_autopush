SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK_SALES S JOIN BOOK B ON S.BOOK_ID = B.BOOK_ID
WHERE YEAR(S.SALES_DATE) = 2022 AND MONTH(S.SALES_DATE) = 1
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC;