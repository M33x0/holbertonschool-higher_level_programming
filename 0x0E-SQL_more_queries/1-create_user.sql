-- 1. Root user
-- Create user with all privileges,script should not fail even if the user already exists
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED 
BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* 
TO 'user_0d_1'@'localhost';