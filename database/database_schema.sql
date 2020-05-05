CREATE DATABASE music_app_db;
USE music_app_db;

CREATE TABLE songs(
	id bigint(11) NOT NULL AUTO_INCREMENT,
	name varchar(100),
	PRIMARY KEY (id)
);

CREATE TABLE users(
	id bigint(11) NOT NULL AUTO_INCREMENT,
	username varchar(30),
	password varchar(30),
	uploader tinyint(1),
	PRIMARY KEY (id)
);

CREATE TABLE playlists(
	id bigint(11) NOT NULL AUTO_INCREMENT,
	userid bigint(11),
	title varchar(30),
	PRIMARY KEY (id),
    FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE TABLE playlistsongs(
	id bigint(11) NOT NULL AUTO_INCREMENT,
	playlistid bigint(11),
	songid bigint(11),
	PRIMARY KEY (id),
    FOREIGN KEY (playlistid) REFERENCES playlists(id),
    FOREIGN KEY (songid) REFERENCES songs(id)
);

INSERT INTO users (username, password, uploader) VALUES ("admin", "admin", 1);