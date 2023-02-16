-- creates a database and a user
-- the user only have SELECT privilege granted
-- if database or user already exists, doesn't fail
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost';
