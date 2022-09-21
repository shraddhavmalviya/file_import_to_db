import pymysql.cursors
import pandas as pd
data = pd.read_csv(r'/home/zec/Desktop/mysql/employees_details (1).csv')
df = pd.DataFrame(data)


print("==============================================================================================")
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Shraddha@123',
                             database='test',
                             cursorclass=pymysql.cursors.DictCursor)


mycursor = connection.cursor()

# mycursor.execute("CREATE TABLE Employee(emp_id INT ,emp_name VARCHAR(25),email VARCHAR(25),gender VARCHAR(25),department VARCHAR(30),address VARCHAR(25),salary bigint)")
# connection.commit()
for row in df.itertuples():
    mycursor.execute ( '''
                INSERT INTO Employee(emp_id,emp_name,email,gender,department,address,salary)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                ''',
                   (row.emp_id ,
                   row.emp_name,
                   row.email,
                   row.gender,
                   row.department,
                   row.address,
                   row.salary
                   ))
connection.commit()


