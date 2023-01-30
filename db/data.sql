DROP TABLE IF EXISTS games;
CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    price INTEGER NOT NULL,
    category VARCHAR(60) NOT NULL,
    released INTEGER NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL
);

INSERT INTO games (name, price, category, released)
VALUES
    ('Duty Of Calls 1', 10, 'Shooter', 1),
    ('Duty of Calls 2', 20, 'Shooter', 1),
    ('Duty of Calls 3', 30, 'Shooter', 1),
    ('Duty of Calls 4', 40, 'Shooter', 0),
    ('Craft Miner', 19, 'Sandbox', 1),
    ('Craft Miner 2', 36, 'Sandbox', 0),
    ('League of Rockets', 10, 'Sport', 1),
    ('Football 2020', 1, 'Sport', 1),
    ('Football 2021', 3, 'Sport', 1),
    ('Football 2022', 8, 'Sport', 1),
    ('Football 2023', 40, 'Sport', 1),
    ('Football 2024', 50, 'Sport', 0),
    ('GTA 1 (Grand Travel Adventures)', 10, 'Sport', 1),
    ('GTA 2 (Grand Travel Adventures)', 15, 'Sport', 1),
    ('GTA 3 (Grand Travel Adventures)', 20, 'Sport', 1),
    ('GTA 4 (Grand Travel Adventures)', 25, 'Sport', 1),
    ('GTA 5 (Grand Travel Adventures)', 30, 'Sport', 1),
    ('GTA 6 (Grand Travel Adventures)', 60, 'Sport', 0),
    ('Running Simulator', 30, 'Simulator', 1),
    ('Tennis Simulator', 30, 'Simulator', 1),
    ('Chicken Dipper Simulator', 30, 'Simulator', 0),
    ('Chicken Dipper Simulator: Deluxe Edition', 35, 'Simulator', 0),
    ('Keyboard Simulator', 30, 'Simulator', 1),
    ('Mouse Simulator', 30, 'Simulator', 1),
    ('TV Simulator', 30, 'Simulator', 1),
    ('Door Simulator', 30, 'Simulator', 1);

INSERT INTO users (username, password)
VALUES
    ('admin1', MD5('cheese')),
    ('admin2', MD5('yogurt')),
    ('admin3', MD5('sand'));