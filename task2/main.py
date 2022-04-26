from db_adapter import DBAdapter
from utility import *

adapter = DBAdapter()

# Получим список пользователей
all_users_query = """SELECT * FROM "Users";"""
users = adapter.get_list_from_select_query(
    adapter.get_connection(), all_users_query)

# Получим список компьютеров
all_comps_query = """SELECT * FROM "Computers";"""
computers = adapter.get_list_from_select_query(
    adapter.get_connection(), all_comps_query)

# Вычислим количество компьютеров у каждого пользователя
counter = get_comps_count(users, computers)

# Отобразим всех пользователей и количество компьютеров у каждого
show_users_and_comps_count(counter)

# Отобразим пользователей без компьютеров
show_users_without_comps(counter)

# Отобразим пользователя с максимальным количеством компьютеров
show_max_count_comps(counter)
