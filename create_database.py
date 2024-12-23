import sqlite3

def create_database():
    conn = sqlite3.connect('tetris.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL,
                 score INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
