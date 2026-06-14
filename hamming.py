"""Модуль генерации чисел Хэмминга с использованием трёх очередей."""


from my_queue import Queue
from exceptions import InvalidCountError


class HammingGenerator:
    """
    Генератор чисел Хэмминга с использованием трех очередей.
    На каждом шаге выбирается минимальный элемент из
    голов очередей, что гарантирует возрастание последовательности.
    """

    def __init__(self):
        self.queue_multiply_2 = Queue()
        self.queue_multiply_3 = Queue()
        self.queue_multiply_5 = Queue()
        self.last_generated_number = 1
        self.generated_count = 0

    def reset(self):
        """Сброс генератора в начальное состояние."""
        self.queue_multiply_2 = Queue()
        self.queue_multiply_3 = Queue()
        self.queue_multiply_5 = Queue()
        self.last_generated_number = 1
        self.generated_count = 0

    def initialize_queues(self):
        """Инициализация очередей начальными значениями (2, 3, 5)."""
        self.queue_multiply_2.enqueue(2)
        self.queue_multiply_3.enqueue(3)
        self.queue_multiply_5.enqueue(5)

    def get_min_from_queues(self):
        """Поиск минимального элемента среди голов очередей."""
        minimum_value = self.queue_multiply_2.peek()

        value_from_queue_3 = self.queue_multiply_3.peek()
        if value_from_queue_3 < minimum_value:
            minimum_value = value_from_queue_3

        value_from_queue_5 = self.queue_multiply_5.peek()
        if value_from_queue_5 < minimum_value:
            minimum_value = value_from_queue_5

        return minimum_value

    def remove_from_queues(self, target_value):
        """Удаление значения из всех очередей, где оно встречается."""
        # Число может быть получено разными путями (например, 6 = 2×3),
        # поэтому удаляем его из всех очередей, где оно головное.
        if (not self.queue_multiply_2.is_empty() and
                self.queue_multiply_2.peek() == target_value):
            self.queue_multiply_2.dequeue()

        if (not self.queue_multiply_3.is_empty() and
                self.queue_multiply_3.peek() == target_value):
            self.queue_multiply_3.dequeue()

        if (not self.queue_multiply_5.is_empty() and
                self.queue_multiply_5.peek() == target_value):
            self.queue_multiply_5.dequeue()

    def add_multiples(self, base_value):
        """Добавление кратных значений в очереди (×2, ×3, ×5)."""
        self.queue_multiply_2.enqueue(base_value * 2)
        self.queue_multiply_3.enqueue(base_value * 3)
        self.queue_multiply_5.enqueue(base_value * 5)

    def generate(self, numbers_count):
        """Генерация первых n чисел Хэмминга с использованием трёх очередей."""
        self.validate_count(numbers_count)
        self.initialize_generation()
        return self.generate_sequence(numbers_count)

    def validate_count(self, numbers_count):
        """Проверка корректности количества чисел."""
        if not isinstance(numbers_count, int) or numbers_count < 1:
            raise InvalidCountError(numbers_count)

    def initialize_generation(self):
        """Инициализация генератора и очередей."""
        self.reset()
        self.initialize_queues()
        self.last_generated_number = 1
        self.generated_count = 1

    def generate_sequence(self, numbers_count):
        """Основной цикл генерации последовательности."""
        result_list = [self.last_generated_number]

        while self.generated_count < numbers_count:
            next_value = self.get_min_from_queues()
            self.remove_from_queues(next_value)
            self.add_multiples(next_value)
            self.last_generated_number = next_value
            result_list.append(next_value)
            self.generated_count += 1

        return result_list

    def get_count(self):
        return self.generated_count
