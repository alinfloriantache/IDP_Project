CREATE DATABASE music_app_db;
USE music_app_db;

CREATE TABLE songs(
	id bigint(11) NOT NULL AUTO_INCREMENT COMMENT "Primary key",
	title varchar(30) COMMENT "Title of the song",
	artists varchar(50) COMMENT "Artists of the song",
	PRIMARY KEY (id)
);