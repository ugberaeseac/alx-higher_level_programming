-- creates the table id_not_null on the MySQL server
-- if table already exists, script should not fail
-- id column must have a default value of 1

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
