-- Task 2: Create database hbtn_0d_2 and user user_0d_2 with SELECT privilege only

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';

-- Create user user_0d_2@localhost with password if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'

-- Grant only SELECT privilege on hbtn_0d_2 to user_0d_2@localhost
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
