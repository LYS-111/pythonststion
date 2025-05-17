# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '0987654321',
    database = 'myweb',
    buffered = True
    )


cursor = conn.cursor()  #建立一個資料庫操作物件


