import mysql.connector


def connect_to_database(host, user, password, database):
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(host=host, user=user, password=password)
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print("Database created successfully")

        # Connect to the specified database
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        print("Connected to the database")

        return connection

    except mysql.connector.Error as err:
        print("Error:", err)
