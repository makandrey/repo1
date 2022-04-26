# Табличный вид. Взято с https://github.com/SuperMaZingCoder/TableIt
import table_it

# Заголовок для таблиц
header = ["Пользователь", "Количество"]

# Возвращает список со списками количества компьютеров у каждого пользователя
def get_comps_count(users, computers):
    counter = []
    for row in users:
        count = 0
        id = row[0]
        name = row[1]
        for row in computers:
            id_user = row[1]
            if id == id_user:
                count += 1
        counter.append([name, count])
    return counter

# Отображает таблицу с количеством компьютеров у каждого пользователя
def show_users_and_comps_count(counter):
    tempList = []
    tempList.append(header)
    tempList.extend(counter)
    print("=======================================")
    print("Количество компьютеров у пользователей:")
    table_it.printTable(tempList, useFieldNames=True)

# Отображает таблицу со списком пользователей без компьютеров
def show_users_without_comps(counter):
    tempList = []
    tempList.append(header)
    for row in counter:
        if row[1] == 0:
            tempList.append(row)
    print("=======================================")
    print("Пользователи без компьютеров:")
    table_it.printTable(tempList, useFieldNames=True)

# Отображает таблицу с наибольшим количеством компьютеров у пользователя
def show_max_count_comps(counter):
    tempList = []
    tempList.append(header)
    max_comps = (max(counter, key=lambda x: x[1]))
    tempList.append(max_comps)
    print("=======================================")
    print("Максимальное количество компьютеров:")
    table_it.printTable(tempList, useFieldNames=True)
