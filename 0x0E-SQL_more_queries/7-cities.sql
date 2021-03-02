-- 7. Cities table
-- create database and table with foreign keys
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY ('state_id') REFERENCES hbtn_0d_usa.states('id')
);