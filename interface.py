from hamming import HammingGenerator
from exceptions import HammingError, InvalidCountError


class ConsoleInterface:
    """Консольный интерфейс для программы генерации чисел Хэмминга."""

    def __init__(self):
        self.generator = HammingGenerator()
        self.is_running = True

    def display_menu(self):
        print("\n" + "=" * 60)
        print(" " * 20 + "ГЛАВНОЕ МЕНЮ")
        print("=" * 60)
        print("  1. Сгенерировать числа Хэмминга")
        print("  2. Информация о программе и примеры")
        print("  3. Выход")
        print("=" * 60)

    def get_user_choice(self):
        """Получение выбора пользователя с валидацией."""
        while True:
            try:
                user_input = input(
                    "\nВведите номер пункта меню (1-3): "
                ).strip()

                if not user_input:
                    print("Ошибка: ввод не может быть пустым")
                    continue

                choice_number = int(user_input)

                if 1 <= choice_number <= 3:
                    return choice_number
                else:
                    print("Ошибка: введите число от 1 до 3")

            except ValueError:
                print("Ошибка: введите корректное число")
            except KeyboardInterrupt:
                print("\n\nПрограмма завершена пользователем")
                return 3

    def display_results(self, generated_numbers):
        """Форматированный вывод результатов генерации."""
        total_count = len(generated_numbers)

        max_number = max(generated_numbers)
        column_width = len(str(max_number)) + 1

        if column_width > 6:
            numbers_per_line = 6
        elif column_width > 5:
            numbers_per_line = 8
        else:
            numbers_per_line = 10

        line_width = numbers_per_line * column_width + (numbers_per_line - 1)

        print("\n" + "-" * line_width)
        print(" " * (line_width // 2 - 9) + "РЕЗУЛЬТАТЫ ГЕНЕРАЦИИ")
        print("-" * line_width)

        for start_index in range(0, total_count, numbers_per_line):
            line_numbers = generated_numbers[
                start_index:start_index + numbers_per_line
            ]
            formatted_line = " ".join(
                f"{num:{column_width}d}"
                for num in line_numbers
            )
            print(formatted_line)

        print("-" * line_width)
        print(f"Всего сгенерировано чисел: {total_count}")
        print(f"Первое число: {generated_numbers[0]}")
        print(f"Последнее число: {generated_numbers[-1]}")
        print("-" * line_width)

    def get_numbers_count(self):
        """Получение количества чисел для генерации."""
        while True:
            try:
                user_input = input(
                    "\nВведите количество чисел (n >= 1): "
                ).strip()

                if not user_input:
                    print("Ошибка: ввод не может быть пустым")
                    continue

                requested_count = int(user_input)

                if requested_count < 1:
                    print("Ошибка: число должно быть больше или равно 1")
                    continue

                if requested_count > 10000:
                    print(
                        "Предупреждение: большое значение может занять время"
                    )

                    while True:
                        confirmation = input(
                            "Продолжить? (y/n/да/нет): "
                        ).strip().lower()

                        if confirmation in ('y', 'yes', 'да', 'д'):
                            return requested_count
                        elif confirmation in ('n', 'no', 'нет', 'н'):
                            break
                        else:
                            print("Пожалуйста, введите y/n или да/нет")
                else:
                    return requested_count

            except ValueError:
                print("Ошибка: введите целое положительное число")
            except KeyboardInterrupt:
                print("\nВвод отменен")
                continue

    def show_info(self):
        """Отображение информации о программе и примеров."""
        print("\n" + "=" * 60)
        print(" " * 15 + "ИНФОРМАЦИЯ О ПРОГРАММЕ")
        print("=" * 60)
        print("\nЧисла Хэмминга (уродливые числа) - это натуральные")
        print("числа, разложение которых на простые множители")
        print("содержит ТОЛЬКО числа 2, 3 и 5.")
        print("\nПримеры разложения:")
        print("  1  = 2^0 * 3^0 * 5^0")
        print("  2  = 2^1 * 3^0 * 5^0")
        print("  3  = 2^0 * 3^1 * 5^0")
        print("  4  = 2^2 * 3^0 * 5^0")
        print("  5  = 2^0 * 3^0 * 5^1")
        print("  6  = 2^1 * 3^1 * 5^0")
        print("  8  = 2^3 * 3^0 * 5^0")
        print("  9  = 2^0 * 3^2 * 5^0")
        print(" 10  = 2^1 * 3^0 * 5^1")
        print(" 12  = 2^2 * 3^1 * 5^0")
        print("\nПример последовательности:")
        print("1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20...")
        print("\nАлгоритм использует три очереди для эффективной")
        print("генерации чисел в порядке возрастания.")
        print("=" * 60)

        input("\nНажмите Enter для возврата в меню...")

    def handle_generate(self):
        """Обработка опции генерации чисел."""
        requested_count = self.get_numbers_count()

        if requested_count is None:
            return

        try:
            generated_numbers = self.generator.generate(requested_count)
            self.display_results(generated_numbers)

            input("\nНажмите Enter для возврата в меню...")

        except InvalidCountError as error_message:
            print(f"\nОшибка: {error_message}")
            input("\nНажмите Enter для продолжения...")
        except HammingError as error_message:
            print(f"\nОшибка генерации: {error_message}")
            input("\nНажмите Enter для продолжения...")
        except Exception as error_message:
            print(f"\nНепредвиденная ошибка: {error_message}")
            input("\nНажмите Enter для продолжения...")

    def handle_exit(self):
        print("\nСпасибо за использование программы!")
        print("До свидания!\n")
        self.is_running = False

    def run(self):
        """
        Запуск главного цикла программы.
        Цикл продолжается до выбора пользователем опции выхода.
        После каждого действия возвращается в меню.
        """
        print("\n" + "=" * 60)
        print(" " * 10 + "ГЕНЕРАТОР ЧИСЕЛ ХЭММИНГА")
        print("=" * 60)

        while self.is_running:
            self.display_menu()
            user_choice = self.get_user_choice()

            if user_choice == 1:
                self.handle_generate()
            elif user_choice == 2:
                self.show_info()
            elif user_choice == 3:
                self.handle_exit()
