# Class-Database-Python
Класс подключения и обращения к базе данных на языке Python

Скачайте эти два файла и разместите в корневой директории приложения

<h1>Подключение</h1>

from loader import db

<h1>Использование</h1>

Выбрать данные
        
        db.fetchall("SELECT * from table")
        
Вставить данные
        
        db.query('INSERT INTO users VALUES (?, ?, ?, ?)', (id, name, login, password))
        
Обновить данные
        
        db.query("UPDATE table SET id = '{0}' WHERE order_id='{1}'".format(id, order_id))
        
Удалить
        
        db.query("DELETE FROM table WHERE id='{0}'".format(user))
