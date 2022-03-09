import sqlite3
from sqlite3 import Error

def main():
    database = r"./sqlite/db/cravingcounter.db"

    sql_create_members_table = """ CREATE TABLE IF NOT EXISTS SMART_MEMBERS (
                                        ID integer PRIMARY KEY,
                                        DISCORD_ID integer NOT NULL,
                                        DISCORD_NAME text,
                                        URGE_COUNT integer,
                                        TIMES_SAID_NO integer
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create members table
        create_table(conn, sql_create_members_table)
    else:
        print("Error! cannot create the database connection.")

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

main()
