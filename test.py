import unittest
import sqlite3
from tetris import TetrisApp

class TestTetris(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             username TEXT UNIQUE NOT NULL,
                             password TEXT NOT NULL,
                             score INTEGER DEFAULT 0)''')
        self.cursor.execute("INSERT INTO users (username, password, score) VALUES ('test_user', 'test_pass', 0)")
        self.conn.commit()
        self.app = TetrisApp('test_user')

    def tearDown(self):
        self.conn.close()

    def test_save_score(self):
        self.app.score = 100
        self.app.save_score()
        self.cursor.execute("SELECT score FROM users WHERE username = 'test_user'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 100)

    def test_game_over(self):
        self.app.score = 150
        self.app.game_over()
        self.cursor.execute("SELECT score FROM users WHERE username = 'test_user'")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 150)

    def test_show_leaderboard(self):
        self.cursor.execute("INSERT INTO users (username, password, score) VALUES ('user1', 'pass1', 200)")
        self.cursor.execute("INSERT INTO users (username, password, score) VALUES ('user2', 'pass2', 150)")
        self.conn.commit()
        self.app.show_leaderboard()

if __name__ == '__main__':
    unittest.main()
