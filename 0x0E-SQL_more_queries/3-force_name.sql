-- creates the table force_name on the MySQL server
-- if table already exists, script should not fail
-- name column must not have a NULL value

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);

