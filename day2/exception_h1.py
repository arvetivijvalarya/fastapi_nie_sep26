import pymysql

try:
    connection = pymysql.Connect(user='nithin', password='root123', database='student', port=3306, host='localhost:3306')
    print('Database connected')
except:
    print('Error in connecting to the database')