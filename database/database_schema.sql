CREATE DATABASE music_app_db;
USE music_app_db;

CREATE TABLE songs(
	id bigint(11) NOT NULL AUTO_INCREMENT,
	title varchar(30),
	artists varchar(50),
	PRIMARY KEY (id)
);