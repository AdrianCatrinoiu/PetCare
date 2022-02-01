import sqlite3 as sql

class DB:
    my_db = sql.connect("myDB.db")
    c = my_db.cursor()

    @classmethod
    def createTables(cls):
        try:
            cls.c.execute('''
                CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author_id INTEGER NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                FOREIGN KEY (author_id) REFERENCES user (id)
                );''')

            cls.c.execute('''
                CREATE TABLE IF NOT EXISTS temperature (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                level REAL NOT NULL
                );''')
            
            cls.c.execute('''
                CREATE TABLE  IF NOT EXISTS food (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                changed_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                level REAL NOT NULL
                );''')

            cls.c.execute('''
                CREATE TABLE IF NOT EXISTS water (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                changed_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                level REAL NOT NULL
                );''')
        except:
            pass

    @classmethod
    def addInTable(cls,table, data):
        if table == 'Water':
            cls.c.execute('insert into water(level) values(?)',(data))
        if table == 'Food':
            cls.c.execute('insert into food(level) values(?)',(data))
        if table == 'Temperature':
            cls.c.execute('insert into temperature(level) values(?)',(data))
    
    def getTableData(cls,table):
        try:
            cls.c.execute(f'select * from {table}')
            return cls.c.fetchall()
        except:
            pass