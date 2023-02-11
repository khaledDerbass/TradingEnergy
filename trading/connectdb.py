from aifc import Error
import sqlite3


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
       # print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = """select * from epex_12_20_12_13"""
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        
        print("SQLite Database Version is: ", record)
        cursor.close()  

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    create_connection(r"c:\Users\Dell\Desktop\kwd\KWD\TradingEnergy\TradingEnergy\trading\trades.db")