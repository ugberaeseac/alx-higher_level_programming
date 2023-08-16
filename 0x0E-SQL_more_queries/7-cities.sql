-- creates the database hbtn_0d_usa and the table cities
-- if the database or table already exists, script should not fail
-- id column must be unique, auto-generated, can't be null and the primary key
-- state_id cant be null and must be a foreign key that references to id
-- of the state table
-- name column can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
	);
