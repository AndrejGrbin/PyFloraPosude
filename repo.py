import sqlite3

def connect_to_database():
    conn = sqlite3.connect("users.db")
    return conn

def close_database_connection(conn):
    conn.close()

def get_user_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    user_data = cursor.fetchone()
    cursor.close()
    return user_data

def update_user_data(conn, new_name, new_surname, new_username, new_password):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET ime=?, prezime=?, user_name=?, password=?", (new_name, new_surname, new_username, new_password))
    conn.commit()
    cursor.close()
