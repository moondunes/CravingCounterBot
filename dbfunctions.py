import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"./sqlite/db/cravingcounter.db")
    except Error as e:
        print(e)
    return conn


def create_member(member):
    conn = create_connection()
    sql = "INSERT INTO SMART_MEMBERS(DISCORD_ID, DISCORD_NAME, URGE_COUNT, TIMES_SAID_NO) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, member)
    conn.commit()
    conn.close()


def update_member(member_name_id, type):
    conn = create_connection()
    set_statement = ''
    if type == 'urge':
        set_statement = 'URGE_COUNT = URGE_COUNT + 1'
    else:
        set_statement = 'TIMES_SAID_NO = TIMES_SAID_NO + 1'
    sql = "UPDATE SMART_MEMBERS SET " + set_statement + " WHERE DISCORD_ID = " + str(member_name_id)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def get_member_data(member_name_id):
    conn = create_connection()
    sql = "SELECT URGE_COUNT, TIMES_SAID_NO FROM SMART_MEMBERS WHERE DISCORD_ID = " + str(member_name_id)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    return result
