import mysql.connector

account = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'crud'
}

connection = mysql.connector.connect(**account)
databaseCursor = connection.cursor()