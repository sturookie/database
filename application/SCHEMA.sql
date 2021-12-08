DROP TABLE IF EXISTS School,Location,Study_Program,School_program;
CREATE TABLE School (
    Campus_Name VARCHAR(127) PRIMARY KEY,
    County VARCHAR(127) REFERENCES Location(County)
    Institution_type VARCHAR(127),
    Institution_level VARCHAR(127),
    Undergraduate_Enrollment INTEGER,
    Graduate_Enrollment INTEGER,
    Campus_Website VARCHAR(127),
);

CREATE TABLE Location (
    County VARCHAR(127) PRIMARY KEY,
    City VARCHAR(127),
    ZIP_CODE VARCHAR(127),
    State VARCHAR(127),
)

CREATE TABLE Study_Program (
    Program_id INTEGER PRIMARY KEY,
    Program_name VARCHAR(127)
)

CREATE TABLE School_program (
    Campus_Name VARCHAR(127) REFERENCES School(Campus_Name),
    Program_id INTEGER REFERENCES Study_Program(Program_id)
)



DROP TABLE IF EXISTS Outdoor;
CREATE TABLE Outdoor (
    Name VARCHAR(127) NOT NULL, 
    Region INTEGER, 
    County VARCHAR(127), 
    Feature VARCHAR(127), 
    Interpretive_Materials VARCHAR(127),
    URL VARCHAR(127),
    UNIQUE(County,Name)
);

DROP TABLE IF EXISTS Food;
CREATE TABLE Food (
   Facility VARCHAR(127) NOT NULL, 
   Address VARCHAR(127),
   Last_inspected timestamp,
   Violations VARCHAR(127),
   ZIP_CODE VARCHAR(127),
   CITY VARCHAR(127),
   County VARCHAR(127),
   Permitted VARCHAR(127),
   Inspection_type VARCHAR(127),
   UNIQUE(Facility, Address)

);

DROP TABLE IF EXISTS Crimes;
CREATE TABLE Crimes(
    County VARCHAR(127),
    Region VARCHAR(127),
    Agency VARCHAR(127),
    Year INTEGER,
    Index_Total VARCHAR(127),
    Violent_Total VARCHAR(127),
    Murder INTEGER,
    Rape INTEGER,
    Robbery INTEGER,
    Aggravated_Assault INTEGER,
    Burglary INTEGER,
    Larceny INTEGER,
    Motor_Vehicle_Theft INTEGER,
    UNIQUE(Agency,Year)
);

