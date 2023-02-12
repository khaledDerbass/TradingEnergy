from aifc import Error
import sqlite3
from django.db.models import Sum

# Note: Kindly see the comments below >> 

# Declare a global variables to sum the total income depends on strategyId and the side of the trade 
total_sell=0  
total_buy=0


def create_connection(db_file):
    # create a database connection to a SQLite database 
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        print("Database created and Successfully Connected to SQLite")

#       sell_select_Query = """SELECT SUM(price*quantity) AS totalprice FROM epex_12_20_12_13 E WHERE E.side=sell AND E.strategy=E.strategy"""
#       sell_select_Query = """SELECT SUM(price*-quantity) AS totalprice FROM epex_12_20_12_13 E WHERE E.side=buy AND E.strategy=E.strategy"""
         
#       When execute the last command it will get exception there's no sell or buy value in side, I know it can solve but Unfortunately there's no time 
      
        sell_select_Query = """SELECT SUM(price*quantity) AS totalprice FROM epex_12_20_12_13 E WHERE E.strategy=E.strategy"""
        buy_select_Query = """SELECT SUM(price*-quantity) AS totalprice FROM epex_12_20_12_13 E WHERE E.strategy=E.strategy"""

        cursor.execute(sell_select_Query)
        total_sell = cursor.fetchall()

        cursor.execute(buy_select_Query)
        total_buy = cursor.fetchall()

        print('Total income sell trades : ',total_sell)
        print('Total income buy trades: ',total_buy)

        cursor.close()  

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    create_connection(r"c:\Users\Dell\Desktop\kwd\KWD\TradingEnergy\TradingEnergy\trading\trades.db")
    