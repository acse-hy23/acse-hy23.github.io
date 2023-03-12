SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
    conditions LIKE 'DIAB1%'
    OR conditions LIKE '% DIAB1%' 

-- 正则
SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
    conditions REGEXP '^DIAB1|\\sDIAB1'