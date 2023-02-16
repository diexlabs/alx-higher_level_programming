-- creates a user with password set to user_0d_1_pwd
-- user have all privileges set
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
