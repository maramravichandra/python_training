from distributed.utils_test import throws

from com.db.postgres_driver import PostgresDriver
import os

host = "localhost" #input("Enter host:")
username = "postgres" #input("Enter username:")
password = "vals@1230" #input("Enter password:")
dbname = "practice" #input("Enter dbname:")
psql_driver = PostgresDriver(host, username, password, dbname)

employee_file_path = "C:\\Users\\mravi\\Personal\\work\\python_training\\resources\\employee.csv" #input("Enter employee.csv file path:")
if os.path.exists(employee_file_path) is False:
    throws(f"{employee_file_path} not found. Exiting..")

emp_file = open(employee_file_path)
for line in emp_file:
    values = line.split(',')
    psql_driver.insert_data(f"{values[0]},'{values[1]}','{values[2]}',{values[3]}")

emp_file.close()

data = psql_driver.read_data("Select * from employee")
for record in data:
    print(record)

data = psql_driver.read_data("Select count(*) from employee")
for record in data:
    print("Record Count :", record)

data = psql_driver.read_data("Select max(sal) as max_sal from employee")
for record in data:
    print("Max Salary :", record)

psql_driver.close_connection()

