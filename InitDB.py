# this project only needs a connection to mysql server and create its own database
# this file will only run once and run the sql script file
import os
import mysql.connector
import json

config = json.load(open('config.json'))
sql_init_script = open('InitDB.sql', 'r').read()


def __init_db__():
    if not os.path.isfile('db_created.txt'):
        f = open('db_created.txt', 'w')
        f.close()

        print("=================== creating database ======================")
        try:
            connection = mysql.connector.connect(
                host=config['host'],
                port=config['port'],
                user=config['user'],
                password=config['password'])

            cursor = connection.cursor()
            result_array = cursor.execute(sql_init_script, multi=True)
            for res in result_array:
                if res.with_rows:
                    print("-------------------------------")
                    print('result:', res.fetchall())

            print("-------------------------------")
            connection.commit()
            connection.close()
        except mysql.connector.Error as e:
            print(e)
        except Exception as e:
            print(e)
