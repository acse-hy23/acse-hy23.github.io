SELECT
    user_id,
    concat(
        upper(left(name, 1)),
        lower(right(name, length(name) -1))
    ) AS name
FROM
    Users