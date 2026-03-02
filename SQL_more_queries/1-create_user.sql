-- Task 1: Create user user_0d_1 with all privileges

-- Create user user_0d_1@localhost with password if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the server to user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
