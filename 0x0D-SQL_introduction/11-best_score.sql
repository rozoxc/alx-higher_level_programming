--  script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Script to list all records of the table second_table in the database hbtn_0c_0 in your MySQL server
-- Select all columns from the second_table and order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
