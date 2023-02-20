import json
import mysql.connector

with open("employees.json") as f:
    employees_data = json.load(f)


connection = mysql.connector.connect(user="root",
                              password='password',
                              host='localhost',
                              database='employees_db')

with connection.cursor() as cursor:

    for employee in employees_data:
        sql = f"insert into employees(name, age, salary) values ('{employee['name']}'," \
              f"{employee['age']}, {employee['salary']})"
        print(employee, sql)
        cursor.execute(sql)
    connection.commit()

connection.close()
