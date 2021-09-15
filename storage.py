import sqlite3 as lite
import threading

lock = threading.Lock()

class DatabaseManager(object):

    def __init__(self, path):
        self.conn = lite.connect(path, check_same_thread=False)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    #Создаем таблицу, если ее нет
    def create_tables(self):
        self.query('CREATE TABLE IF NOT EXISTS users (cid int, name text, level int, verification int)')

    def query(self, arg, values=None):
        if values == None:
            with lock:
                self.cur.execute(arg)
        else:
            with lock:
                self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            with lock:
                self.cur.execute(arg)
        else:
            with lock:
                self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values == None:
            with lock:
                self.cur.execute(arg)
        else:
            with lock:
                self.cur.execute(arg, values)
        return self.cur.fetchall()


    def __del__(self):
        self.conn.close()
