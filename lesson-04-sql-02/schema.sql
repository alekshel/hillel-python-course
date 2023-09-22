DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS tracks;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

CREATE TABLE tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author VARCHAR(100) NOT NULL,
    duration INTEGER NOT NULL,
    date_publicated DATE NOT NULL
);