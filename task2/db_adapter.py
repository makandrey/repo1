import psycopg2
from conf import *

# Класс для работы с БД
class DBAdapter:

    # Создает и если успешно возвращает соединение с БД
    def get_connection(self):
        try:
            connection = psycopg2.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DBNAME
            )
            connection.autocommit = True
        except Exception as _ex:
            print("[ERROR] : Failed to create database connection", _ex)
        finally:
            if connection:
                print('[INFO] : Successful connection to the database}')
                return connection

    # Возвращает результат запроса SELECT в виде списка
    def get_list_from_select_query(self, connection, query):
        list = []
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    query
                )
                list = cursor.fetchall()
        except Exception as _ex:
            print("[ERROR] : An error occurred while executing the query", _ex)
        finally:
            if connection:
                connection.close()
                print('[INFO] : Database connection closed}')
        return list
