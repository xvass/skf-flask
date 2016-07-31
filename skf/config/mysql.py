
from flask import Flask
from flask import g
from flask import Response
from flask import request
import json
import MySQLdb

app = Flask(__name__)

def database_con():
  g.conn = MySQLdb.connect(host='192.168.33.10',
                              user='test',
                              passwd='password',
                              db='test')
  g.cursor = g.conn.cursor()
  return g.conn