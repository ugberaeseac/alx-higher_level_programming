-- creates database hbtn_0d_2 and the user user_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database already exists, the script should not fail
-- If the user user_0d_2 already exists, the script should not fail
-- the user should only have SELECT privilege in the database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
