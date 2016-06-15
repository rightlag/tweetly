DROP DATABASE IF EXISTS twitter;

CREATE DATABASE twitter;

USE twitter;

CREATE TABLE tweets
(
    id INT(11) NOT NULL AUTO_INCREMENT,
    handle VARCHAR(255) NOT NULL,
    tweet VARCHAR(255) NOT NULL,
    fetched VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
