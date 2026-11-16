import psycopg2
from config import load_config


def connect():
    config = load_config()
    conn = psycopg2.connect(**config)
    return conn


if __name__ == "__main__":
    try:
        conn = connect()
        print("Successfully connected to PostgreSQL!")

        conn.close()
        print("Connection closed.")

    except Exception as error:
        print("Connection failed:")
        print(error)