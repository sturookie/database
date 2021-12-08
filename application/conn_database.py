#encoding: utf-8
import psycopg2
import psycopg2.extras
from flask import Flask, redirect,  url_for, request, render_template, flash
from werkzeug.utils import secure_filename

import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
conn = psycopg2.connect(database="postgres",user="postgres",password="3301360",host="127.0.0.1",port="5432")
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # sql="insert into tablename (is_enable,start_time,end_time,reg_name,reg_radius,valid_time,reg_gov,guid,geom) values ('1','{0}','{1}','{2}',{3},'{4}','{5}','{6}',ST_GeomFromGeoJson('{7}'))".format(start_time,end_time,reg_name,reg_radius,valid_time,reg_gov,guid,geom)
    # print(sql)

# sql="select xm,zh from userinfo"
# cursor.execute(sql)
# user = cursor.fetchall()
# row=json.dumps(user,ensure_ascii=False)
# print(row)
# print(user)
conn.commit()
# print('更新成功')