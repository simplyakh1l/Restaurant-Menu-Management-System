CREATE DATABASE IF NOT EXISTS restaurant;
USE restaurant;

CREATE TABLE IF NOT EXISTS menu (
    fid INT PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    rating DECIMAL(2,1) CHECK (rating > 0),
    dor DATE
);
