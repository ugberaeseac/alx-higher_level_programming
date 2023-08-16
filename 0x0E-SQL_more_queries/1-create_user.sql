-- script that creates the MySQL server user user_0d_1
-- if already exists, script should not fail
-- password is user_0d_1_pwd
-- grant all privileges to user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
