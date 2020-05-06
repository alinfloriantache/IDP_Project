import mysql.connector


def get_db_connection():
	config = {
        'user': 'root',
        'password': 'shortpass10',
        'host': 'database',
        'port': '3306',
        'database': 'music_app_db'
    }
	return mysql.connector.connect(**config)