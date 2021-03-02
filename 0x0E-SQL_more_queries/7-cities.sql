-- 7. Cities table
-- create database and table with foreign keys
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT PRIMARY KEY AUTOINCREMENT NOT NULL,
	state_id NOT NULL FOREIGN KEY (state_id) REFERENCES city(id),
	name VARCHAR(256) NOT NULL
);