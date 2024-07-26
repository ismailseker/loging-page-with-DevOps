CREATE DATABASE flaskData;
USE flaskData;


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password, email) VALUES ('john_doe', 'password123', 'john@example.com');
INSERT INTO users (username, password, email) VALUES ('jane_smith', 'password456', 'jane@example.com');
INSERT INTO users (username, password, email) VALUES ('alice_jones', 'password789', 'alice@example.com');

INSERT INTO users (username, password, email, role) VALUES ('admin_username', 'admin_password', 'admin@example.com', 'admin');
INSERT INTO users (username, password, email, role) VALUES ('aziz', 'aziz123', 'aziz@example.com', 'admin');

UPDATE users SET password = 'password123' WHERE username = 'john_doe';
UPDATE users SET password = 'password456' WHERE username = 'jane_smith';
UPDATE users SET password = 'password789' WHERE username = 'alice_jones';

ALTER TABLE users ADD COLUMN role ENUM('admin', 'user') DEFAULT 'user';

-- Var olan kullanıcıyı admin olarak güncelle
UPDATE users SET role='admin' WHERE username='admin_username';
