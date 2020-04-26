from datetime import date,timedelta
from urllib.request import urlopen
from dateutil import rrule
from DB import SQL_Manager
import sqlite3
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import json
import time

class Stock_Crawler():
    def __init__(self):
        self.SQLManager = SQL_Manager()

    def crawl_one_month(self, stockID, date):
        url = ("http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + date.strftime('%Y%m%d') + "&stockNo=" + str(stockID))
        data = json.loads(urlopen(url).read())
        df = pd.DataFrame(data['data'],columns=data['fields'])
        self.SQLManager.insertDataFrameToDB(df)


    def craw_period(self, stockID, start_month, end_month):
        b_month = date(*[int(x) for x in start_month.split('-')])
        e_month = date(*[int(x) for x in end_month.split('-')])
        #now = datetime.datetime.now().strftime("%Y-%m-%d")
        #e_month = date(*[int(x) for x in now.split('-')])
        
        result = pd.DataFrame()
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=b_month, until=e_month):
            result = pd.concat([result,self.crawl_one_month(stockID,dt)],ignore_index=True)
            time.sleep(2000.0/1000.0)  
        return result