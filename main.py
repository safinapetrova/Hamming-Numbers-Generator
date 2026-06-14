"""Точка входа в программу генерации чисел Хэмминга."""

from interface import ConsoleInterface


def main():
    """Главная функция программы. Запускает цикл меню."""
    console_interface = ConsoleInterface()
    console_interface.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма завершена пользователем")
        print("До свидания!\n")
