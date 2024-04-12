import mysql.connector


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("Error executing query:", err)
