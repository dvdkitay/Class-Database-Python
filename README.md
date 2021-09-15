# Class-Database-Python
Класс подключения и обращения к базе данных на языке Python

Скачайте эти два файла и разместите в корневой директории приложения

<h1>Подключение</h1>

<li>from loader import db

<h1>Использование</h1>

1. Выбрать данные
        
        db.fetchall("SELECT * from table")
2. Вставить данные
        db.query("INSERT INTO table VALUES '{0}'".format(id)
3. Обновить данные
        db.query("UPDATE table SET id = '{0}' WHERE order_id='{1}'".format(id, order_id))
4. Удалить
        db.query("DELETE FROM table WHERE id='{0}'".format(user))
