from typing import Match, NewType
import time
import sqlite3
from ansicolors import colors
#######################
#SQLITE3 DATABASE
#create the sqlite3 database
db_conn = sqlite3.connect("test.db")
print("database Connected")
theCursor = db_conn.cursor()
print(theCursor.arraysize)

def print_user_from_Db(userShape):
    try:
        result = theCursor.execute("SELECT Id, FName, LName, Age, Address, Salary, HireDate from Employees WHERE FName = '{}' and Salary = '{}'".format(userShape["firstName"], userShape["salary"]))
        for row in result:
            print(colors.reset,"ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
            print("####################################")
    except Exception as e:
        print(e)

def print_DB():
    try:
        result = theCursor.execute("SELECT Id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
            print("####################################")
    except sqlite3.OperationalError:
        print("The tables doesnt exist")
    except: 
        print("couldnt get data")


def create_db():
    try:
        #every run will wipe database
        db_conn.execute("DROP TABLE IF EXISTS Employees")

        #table create function
        db_conn.execute("Create Table Employees(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LNAME TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

        db_conn.commit()
        print("Table was created")
    except sqlite3.OperationalError:
        print("table not created")

create_db()

def get_time():
    return time.strftime("%m/%d/%Y", time.gmtime())

print('Create a database entry? y / n')
newUser = input()

if newUser == 'y':
    userData={
    "firstName":'',
    "lastName": '',
    "age": 0,
    "address": " ",
    "salary": 0,
    "hireDate": '',
    "confirmationMsg": ''
    }
    print('Your first name')
    userData["firstName"] = input()

    print('Your last name')
    userData["lastName"] = input()

    print('Your age')
    userData["age"] = input()

    print('Your address')
    userData["address"] = input()

    print('Your salary')
    userData["salary"] = input()
    userData["hireDate"] = get_time()
    
    userData["confirmationMsg"] = '''
        Your profile is as follows:
        first name: {} \n
        last name: {} \n
        age: {}.\n
        address: {}\n
        salary: {}\n
        hire date: {} \n
        '''.format(
            userData["firstName"],
            userData["lastName"],
            userData["age"],
            userData["address"],
            userData["salary"], 
            userData["hireDate"], 
            )

    print(colors.fgCyan,userData["confirmationMsg"])
    print(colors.reset,"Is this correct? (y / n)")
    proceed= input()
    if proceed == 'y':
        try:
            db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)" "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(userData["firstName"], userData["lastName"], userData["age"], userData["address"], userData["salary"], userData["hireDate"]))
            db_conn.commit()
            print(userData["firstName"] + userData["lastName"] + " added to the database")
        except Exception as e: print('big time error :', e)

#insertion function
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)" "VALUES ('Dominique', 'Sakrisson', 27, '123 main st', '500,000,000', date('now'))")
db_conn.commit()
print_DB()
getUser= 'n'
print("would you like to view a user? (y / n)")
getUser = input()
while getUser == 'y':
    userShape= {
        "firstName": "",
        "salary": "",
    }
    print(colors.fgCyan,"user first name")
    userShape["firstName"] = input()
    print("user salary")
    userShape["salary"] = input()
    
    print_user_from_Db(userShape)

    print("would you like to view another user? (y / n)")
    getUser = input()

      
# execute printDb to return all results from database employees
db_conn.close()
