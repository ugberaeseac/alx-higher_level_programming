-- creates the database hbtn_0d_usa and the table states
-- if the database or table already exists, script should not fail
-- id column must be unique, auto-generated, can't be null and the primary key
-- name column can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);
