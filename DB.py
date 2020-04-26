import pandas as pd  
import sqlite3

class SQL_Manager():
    def __init__(self, db_path="Stock.db"):
        self._db_path = db_path
        self.createTable("1101")

    def createTable(self, tableName):
        with sqlite3.connect(self._db_path) as conn:
            try:
                # 日期(Key) | 成交股數 | 成交金額 | 開盤價 | 最高價 | 最低價 | 收盤價 | 漲跌幅 | 成交筆數
                tableStruct = '''
                (Date       TEXT PRIMARY KEY     NOT NULL,
                TV          INT                  NOT NULL,
                TS          INT                  NOT NULL,
                OP          REAL                 NOT NULL,
                HP          REAL                 NOT NULL,
                LP          REAL                 NOT NULL,
                CP          REAL                 NOT NULL,
                Change      REAL                 NOT NULL,
                Num         INT                  NOT NULL
                )'''
                conn.execute("CREATE TABLE IF NOT EXISTS" + tableName + "(" + tableStruct + ")")
                return True
            except:
                return False

    def selectTable(self, tableName):
        with sqlite3.connect(self._db_path) as conn:
            try:
                cur = conn.cursor().execute("SELECT * FROM " + tableName)
                return cur.fetchall()

            except:
                return "Fail!"
    
    def selectTableWithCondition(self, tableName, condition):
        with sqlite3.connect(self._db_path) as conn:
            try:
                cur = conn.cursor().execute("SELECT * FROM " + tableName + "WHERE " + condition)
                return cur.fetchall()

            except:
                return "Fail!"

    def insertDataFrameToDB(self, data):
        with sqlite3.connect(self._db_path) as conn:
            pd.io.sql.to_sql(data, "1101", con = conn, if_exists="append", index=False)