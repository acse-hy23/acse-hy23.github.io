DELETE p1
FROM
    Person p1,
    Person p2
WHERE
    p1.email = p2.email
    AND p1.id > p2.id 
    
-- 使用了子查询，p是一个临时表，不能先select出同一表中的某些值，再update这个表(在同一语句中)。可以将SELECT出的结果再通过中间表SELECT一遍
DELETE FROM
    Person
WHERE
    id NOT IN (
        SELECT
            id
        FROM
            (
                SELECT
                    MIN(id) AS id
                FROM
                    Person
                GROUP BY
                    email
            ) p
    );