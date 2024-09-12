import sqlite3

# Classe para agenciar a conexão com BD SQLite
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL                    
    )
        ''')
        self.conn.commit()