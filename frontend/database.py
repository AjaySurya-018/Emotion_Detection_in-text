# Load Database Packages
import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='DB',
            user='ajay',
            password='ajay'
        )
        if connection.is_connected():
            print(f'Connected to MySQL Server (Version: {connection.get_server_info()})')
            return connection
    except Error as e:
        print(f'Error: {e}')
        return None

# Function to create a table for page tracking
def create_page_visited_table():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pageTrackTable (
                pagename VARCHAR(255),
                timeOfvisit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        connection.commit()
        cursor.close()
        connection.close()

# Function to add page visit details to the MySQL database
def add_page_visited_details(pagename):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO pageTrackTable(pagename) VALUES(%s)', (pagename,))
        connection.commit()
        cursor.close()
        connection.close()

# Function to view all page visit details from the MySQL database
def view_all_page_visited_details():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pageTrackTable')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data

# Function to create a table for emotion classifier tracking
def create_emotionclf_table():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emotionclfTable (
                rawtext TEXT,
                prediction TEXT,
                probability FLOAT,
                timeOfvisit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        connection.commit()
        cursor.close()
        connection.close()

# Function to add emotion classifier prediction details to the MySQL database
def add_prediction_details(rawtext, prediction, probability):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability) VALUES(%s, %s, %s)', (rawtext, prediction, probability))
        connection.commit()
        cursor.close()
        connection.close()

# Function to view all emotion classifier prediction details from the MySQL database
def view_all_prediction_details():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM emotionclfTable')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data
