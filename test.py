# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:09:56 2016

@author: Yuxuan
"""
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()


statement = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 3'''

for row in cur.execute(statement):
    print(row)
