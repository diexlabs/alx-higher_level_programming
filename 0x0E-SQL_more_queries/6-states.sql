-- creates a states database and table
-- sets constraint for id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE
	IF NOT EXISTS hbtn_0d_usa.states (
		id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
		name VARCHAR(256) NOT NULL
	);