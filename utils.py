import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--pguser")
parser.add_argument("--pgpass")
parser.add_argument("--host")
parser.add_argument("--port")
parser.add_argument("--db")


def connect_postgres(username, user_password, host_adress, user_port, user_db):
    try:
        connection = psycopg2.connect(user=username,
                                      password=user_password,
                                      host=host_adress,
                                      port=user_port,
                                      database=user_db)

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")