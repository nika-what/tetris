import registration
import login
import tetris

def main():
    registration.run_registration()  # Открываем регистрацию или вход
    login.run_login()  # Запускаем вход и получаем имя пользователя

if __name__ == "__main__":
    main()
