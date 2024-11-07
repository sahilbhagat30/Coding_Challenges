SELECT
    P.NAME,
    ROUND(COUNT(C.PROPERTY_ID),2),
    ROUND(MIN(C.AMOUNT),2),
    ROUND(MAX(C.AMOUNT),2),
    ROUND(AVG(C.AMOUNT),2)
FROM 
    PROPERTIES P
JOIN 
    CASH_FLOWS C ON P.ID = C.ID
GROUP BY
    1
HAVING 
     AVG(C.AMOUNT) > 10000

ORDER BY 
    1

    