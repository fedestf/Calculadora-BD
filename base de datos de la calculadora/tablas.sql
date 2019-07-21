create schema if not exists calculadora;
use calculadora;

CREATE TABLE test (
    id INT PRIMARY KEY AUTO_INCREMENT,
    calculo VARCHAR(20),
    resultado INT
);
select * from test;
CREATE TABLE suma (
    id INT PRIMARY KEY AUTO_INCREMENT,
    calculo VARCHAR(20),
    resultado INT
);

CREATE TABLE resta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    calculo VARCHAR(20),
    resultado INT
);

CREATE TABLE multiplicacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    calculo VARCHAR(20),
    resultado INT
);
CREATE TABLE division (
    id INT PRIMARY KEY AUTO_INCREMENT,
    calculo VARCHAR(20),
    resultado INT
);