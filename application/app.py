from flask import Flask
import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
from flask import Flask, redirect,  url_for, request, render_template, flash
from werkzeug.utils import secure_filename

import json
import psycopg2.extras


from flask import Flask,session
from datetime import timedelta
import os

# os.system('ipconfig/all')
import conn_database
conn = psycopg2.connect(database="postgres",user="postgres",password="3301360",host="localhost",port="5432")
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
# cursor =conn_database.con.cursor()
# # print(json.dumps(conn_database.row,ensure_ascii=False))
# sql ="select * from userinfo where zh=20210000"
# #执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# cursor.execute(sql)
# #返回一条结果行
# row=cursor.fetchone()
# #接收全部的返回结果行.row里保存的将会是查询返回的全部结果.每条结果都是一个tuple类型的数据,
# row=json.dumps(row,ensure_ascii=False)
# print(row)


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'hello world'
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1',port=5000)
#
# app = Flask(__name__)
# run_with_ngrok(app)
# 两种方式设置secret_key
# app.secret_key = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
# @app.route('/',methods=['GET','POST'])
# def hello_world():
#     session['username']='saber'
#     # session permanent 持久化置为True则session课保存31天.
#     session.permanent = True
#     return render_template("login/hello.html")
cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
@app.route("/")
def home():
    sql = "select school.campus_name,study_program.program_id,school.county,institution_type,city,state from School,Location, study_program, School_program where School.County = Location.County and School.Campus_Name = School_program.Campus_Name"
    cursor.execute(sql)
    user = cursor.fetchall()
    rows = json.dumps(user, ensure_ascii=False)
    print(rows)
    return render_template("data_show/index.html",rows=rows)

@app.route("/view")
def view():
    name = request.args.get('name')
    sql_crimes ="select count(*) as total from school,crimes where lower(school.county)=lower(crimes.county) and campus_name='"+name+"'"
    cursor.execute(sql_crimes)
    crimes = cursor.fetchone()
    crimes =crimes['total']
    sql_food = "select count(*) as total from school,food where lower(school.county)=lower(food.county) and campus_name='" + name + "'"
    cursor.execute(sql_food)
    food = cursor.fetchone()
    food = food['total']
    sql_recreation = "select count(*) as total from school,outdoor where lower(school.county)=lower(outdoor.county) and campus_name='" + name + "'"
    cursor.execute(sql_recreation)
    outdoor = cursor.fetchone()
    outdoor = outdoor['total']
    return render_template("data_show/view.html",crimes=crimes,food=food,outdoor=outdoor)


if __name__ == "__main__":
    app.run()





