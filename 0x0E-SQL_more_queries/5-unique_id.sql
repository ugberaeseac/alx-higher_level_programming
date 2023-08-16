-- creates the table unique_id on the MySQL server
-- if table already exists, script should not fail
-- id column must have a default value of 1 and must be unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
