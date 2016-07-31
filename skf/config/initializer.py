#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('Database.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Users(UserId INT, UserName TEXT, Password TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Riiecco','$2b$12$hB5keCvwP1Ukx/XHKRs.tu/g5e7DZrJ27PP4MFGsk57tZEy3O618O')")
    cur.execute("CREATE TABLE Projects(ProjectId INT, ProjectName TEXT, ProjectVersion TEXT, ProjectDescription TEXT, UserId INT)")
    cur.execute("INSERT INTO Projects VALUES(1,'Test','1.1', 'test project desc', 1)")
    con.commit()
    con.close()