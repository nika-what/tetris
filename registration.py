from tkinter import *
from tkinter import messagebox
import sqlite3
import login

def run_registration():
    root = Tk()
    root.geometry('400x400')
    root.title('Registration')
    root.configure(bg='#f0f0f0')

    def create_db():
        connection = sqlite3.connect('tetris.db')
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            score INTEGER DEFAULT 0
        )
        ''')
        connection.commit()
        connection.close()

    def registration():
        def save():
            username = registr_username.get()
            password = registr_password.get()
            if not username or not password:
                messagebox.showwarning('Error', 'Username and password cannot be empty!')
                return
            try:
                connection = sqlite3.connect('tetris.db')
                cursor = connection.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                connection.commit()
                messagebox.showinfo('Success', 'Registration successful!')
                root.quit()  # Закрываем окно регистрации и возвращаем управление в main.py
            except sqlite3.IntegrityError:
                messagebox.showwarning('Error', 'This username is already taken!')
            except Exception as e:
                messagebox.showerror('Error', f'An error occurred: {e}')
            finally:
                if connection:
                    connection.close()

        # Рамка для элементов регистрации
        frame = Frame(root, bg='#ffffff', padx=20, pady=20)
        frame.pack(fill=BOTH, expand=True)

        # Элементы интерфейса для регистрации
        title_label = Label(frame, text='Registration', font=('Helvetica', 24), bg='#ffffff', fg='#333333')
        title_label.pack(pady=(20, 10))

        text_username = Label(frame, text='Enter your username:', bg='#ffffff', fg='#333333', font=('Helvetica', 14))
        text_username.pack(anchor='w', padx=20)

        registr_username = Entry(frame, width=30, font=('Helvetica', 14))
        registr_username.pack(pady=(0, 10), padx=20)

        text_password = Label(frame, text='Enter your password:', bg='#ffffff', fg='#333333', font=('Helvetica', 14))
        text_password.pack(anchor='w', padx=20)

        registr_password = Entry(frame, show='*', width=30, font=('Helvetica', 14))
        registr_password.pack(pady=(0, 20), padx=20)

        button_registr = Button(frame, text='Register', command=save, bg='#4CAF50', fg='white', font=('Helvetica', 14))
        button_registr.pack(pady=10)

        # Кнопка для перехода к окну входа
        button_login_redirect = Button(frame, text='Already registered? Login!', command=lambda: [root.quit(), login.run_login()], bg='#008CBA', fg='white', font=('Helvetica', 14))
        button_login_redirect.pack(pady=(10, 0))

    # Создание базы данных и таблицы при запуске приложения
    create_db()

    # Вызов функции регистрации
    registration()

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == "__main__":
    run_registration()
