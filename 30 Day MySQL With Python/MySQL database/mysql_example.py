import mysql.connector
from mysql.connector import Error, pooling
import configparser

def read_config(filename='config.ini', section='mysql'):
    parser = configparser.ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            config[item[0]] = item[1]
    else:
        raise Exception(f"{section} not found in {filename}")

    return config

def execute_query(connection, query, data=None):
    try:
        cursor = connection.cursor()

        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)

        if "SELECT" in query.upper():
            results = cursor.fetchall()
            return results
        else:
            connection.commit()
            return None

    except Error as e:
        print(f"Error: {e}")
        raise

    finally:
        cursor.close()

def main():
    try:
        # Read database configuration from the config file
        db_config = read_config()

        # Create a connection pool
        connection_pool = pooling.MySQLConnectionPool(
            pool_name="example_pool",
            pool_size=5,
            **db_config
        )

        # Acquire a connection from the pool
        connection = connection_pool.get_connection()

        # Example: Creating a table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS example_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """
        execute_query(connection, create_table_query)

        # Example: Inserting data
        insert_data_query = "INSERT INTO example_table (name) VALUES (%s)"
        data_to_insert = ("John Doe",)
        execute_query(connection, insert_data_query, data_to_insert)

        # Example: Retrieving data
        select_data_query = "SELECT * FROM example_table"
        results = execute_query(connection, select_data_query)

        # Displaying results
        print("Data in the 'example_table':")
        for row in results:
            print(row)

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Release the connection back to the pool
        connection.close()

if __name__ == "__main__":
    main()
