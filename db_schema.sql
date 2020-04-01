CREATE TABLE IF NOT EXISTS `songs` (
	`id` bigint(11) UNSIGNED NOT NULL auto_increment COMMENT `Primary key`,
	`title` varchar(30) NOT NULL COMMENT `Title of the song`,
	`artists` varchar(50) NOT NULL COMMENT `Artists of the song`,
) DEFAULT CHARSET=utf8
