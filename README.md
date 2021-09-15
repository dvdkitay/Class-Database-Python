# Class-Database-Python
Класс подключения и обращения к базе данных на языке Python

Скачайте эти два файла и разместите в корневой директории приложения

<h1>Подключение</h1>

<li>from loader import db

<h1>Использование</h1>

<li>1. Выбрать данные
<li>db.fetchall("SELECT * from table")
<li>2. Вставить данные
<li>db.query("INSERT INTO table VALUES '{0}'".format(id)
<li>3. Обновить данные
<li>db.query("UPDATE table SET id = '{0}' WHERE order_id='{1}'".format(id, order_id))
<li>4. Удалить
<li>db.query("DELETE FROM table WHERE id='{0}'".format(user))
