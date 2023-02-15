-- displays records where name is not NULL
-- dispays score and name in order
-- orders by score descending
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
