import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from io import StringIO
import numpy as np
#Import .csv file
university0 = pd.read_csv('State_University_of_New_York__SUNY__Campus_Locations_with_Websites__Enrollment_and_Select_Program_Offerings.csv')
university0['County'] = university0.County.str.lower()
university = university0[['Campus Name','County','Institution Type','Institution Level','Undergraduate Enrollment','Graduate Enrollment','Campus Website']]
recreation = pd.read_csv('Accessible_Outdoor_Recreation_Destinations_Map.csv')
outdoor=recreation[['Name','Region','County','Feature']]
outdoor['County'] = outdoor.County.str.lower()
food0 = pd.read_csv('Food_Service_Establishment_Map__Last_Inspection.csv')
food = food0[['ADDRESS','CITY','COUNTY']]
food = food.drop(7920, axis=0)
food['COUNTY'] = food.COUNTY.str.lower()
crime0 = pd.read_csv('Index_Crimes_by_County_and_Agency__Beginning_1990.csv')
crimes = crime0[['County','Region','Agency','Year','Index Total']]
crimes['County'] = crimes.County.str.lower()
crimes = crimes.dropna(axis=0,how='any')
crimes['Index Total'] = crimes['Index Total'].astype(int)

pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)



location = pd.DataFrame(university0, columns=['County' ,'City', 'Zip','State'])
location =location.drop_duplicates(subset=['County'],keep='first')
program = pd.DataFrame(university0, columns=['Campus Name','Program 1','Program 2','Program 3','Program 4','Program 5'])

program =pd.melt(program,id_vars=['Campus Name'],value_name='Program_name')



Study_Program = pd.DataFrame(program,columns=['Campus Name','Program_name'])
program_id = []
for i in range(len(Study_Program)):
    program_id.append(i+1)
program_id = np.array(program_id)

Study_Program.insert(1,'Program_id',program_id)

School_Program = Study_Program.copy()
Study_Program = Study_Program.drop(columns = ['Campus Name'])


School_Program =School_Program.drop(columns = ['Program_name'])
School_Program = School_Program.sort_values(by = 'Campus Name')




output = StringIO()
university.to_csv(output, sep='\t', index=False, header=False)
output1 = output.getvalue()

output2 = StringIO()
location.to_csv(output2, sep='\t', index=False, header=False)
output3 = output2.getvalue()

output4 = StringIO()
Study_Program.to_csv(output4, sep='\t', index=False, header=False)
output5 = output4.getvalue()

output6 = StringIO()
School_Program.to_csv(output6, sep='\t', index=False, header=False)
output7 = output6.getvalue()

output8 = StringIO()
outdoor.to_csv(output8, sep='\t', index=False, header=False)
output9 = output8.getvalue()

output10 = StringIO()
food.to_csv(output10, sep='\t', index=False, header=False)
output11 = output10.getvalue()

output12 = StringIO()
crimes.to_csv(output12, sep='\t', index=False, header=False)
output13 = output12.getvalue()

table_create_sql = '''
DROP TABLE IF EXISTS Location,School,Study_Program,School_program,Outdoor,Food,Crimes;
CREATE TABLE Location (
    County VARCHAR(127) PRIMARY KEY,
    City VARCHAR(127),
    ZIP_CODE INTEGER,
    State VARCHAR(127));

CREATE TABLE School (
    Campus_Name VARCHAR(127) PRIMARY KEY,
    County VARCHAR(127) REFERENCES Location(County),
    Institution_type VARCHAR(127),
    Institution_level VARCHAR(127),
    Undergraduate_Enrollment INTEGER,
    Graduate_Enrollment INTEGER,
    Campus_Website VARCHAR(127));

CREATE TABLE Study_Program (
    program_id INTEGER PRIMARY KEY,    
    Program_name VARCHAR(127));

CREATE TABLE School_program (
    Campus_Name VARCHAR(127) REFERENCES School(Campus_Name),
    Program_id INTEGER REFERENCES Study_Program(Program_id));

DROP TABLE IF EXISTS Outdoor;
CREATE TABLE Outdoor (
    Name VARCHAR(127) NOT NULL, 
    Region INTEGER, 
    County VARCHAR(127), 
    Feature VARCHAR(127));

DROP TABLE IF EXISTS Food;
CREATE TABLE Food (
   Address VARCHAR(127),
   CITY VARCHAR(127),
   County VARCHAR(127));

DROP TABLE IF EXISTS Crimes;
CREATE TABLE Crimes(
    County VARCHAR(127),
    Region VARCHAR(127),
    Agency VARCHAR(127),
    Year INTEGER,
    Index_Total BIGINT)
'''
pg_conn = psycopg2.connect(database="postgres", user="postgres", password="3301360", host="127.0.0.1", port="5432")
cur = pg_conn.cursor()
cur.execute(table_create_sql)
cur.copy_from(StringIO(output3),'location')
cur.copy_from(StringIO(output1),'school')#columns=['campus_name', 'county','uni_id'])
cur.copy_from(StringIO(output5),'study_program')
cur.copy_from(StringIO(output7),'school_program')
cur.copy_from(StringIO(output9),'outdoor')
cur.copy_from(StringIO(output11),'food')
cur.copy_from(StringIO(output13),'crimes')
#cur.copy_from(StringIO(output1),'copy_test',columns=['campus_name', 'county'])
#cur.copy_from(StringIO(output1),'copy_test',columns=['campus_name', 'county'])
pg_conn.commit()




#close connection
pg_conn.close()
