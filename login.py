from tkinter import *
from tkinter import messagebox
import sqlite3
import tetris

def run_login():
    root = Tk()
    root.geometry('400x400')
    root.title('Login')
    root.configure(bg='#f0f0f0')

    def login():
        username = login_entry.get()
        password = password_entry.get()
        if not username or not password:
            messagebox.showwarning('Error', 'Username and password cannot be empty!')
            return

        connection = sqlite3.connect('tetris.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo('Success', 'Login successful!')
            root.quit()  # Закрываем окно входа

            # Запускаем игру после успешного входа с передачей логина текущего пользователя в start_game.
            tetris.start_game(username)
        else:
            messagebox.showwarning('Error', 'Invalid username or password!')

        connection.close()

    frame = Frame(root, bg='#ffffff', padx=20, pady=20)
    frame.pack(fill=BOTH, expand=True)

    # Элементы интерфейса для входа
    title_label = Label(frame, text='Login', font=('Helvetica', 24), bg='#ffffff', fg='#333333')
    title_label.pack(pady=(20, 10))

    text_username = Label(frame, text='Enter your username:', bg='#ffffff', fg='#333333', font=('Helvetica', 14))
    text_username.pack(anchor='w', padx=20)

    login_entry = Entry(frame, width=30, font=('Helvetica', 14))
    login_entry.pack(pady=(0, 10), padx=20)

    text_password = Label(frame, text='Enter your password:', bg='#ffffff', fg='#333333', font=('Helvetica', 14))
    text_password.pack(anchor='w', padx=20)

    password_entry = Entry(frame, width=30, font=('Helvetica', 14))
    password_entry.pack(pady=(0, 20), padx=20)

    button_login = Button(frame, text='Login', command=login, bg='#4CAF50', fg='white', font=('Helvetica', 14))
    button_login.pack(pady=(10, 5))

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == "__main__":
    run_login()
