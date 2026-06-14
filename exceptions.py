class HammingError(Exception):
    """Базовое исключение для ошибок генератора Хэмминга."""
    pass


class InvalidCountError(HammingError):
    """Исключение для некорректного количества чисел."""

    def __init__(self, invalid_count_value):
        """Инициализация исключения."""
        self.invalid_count_value = invalid_count_value
        HammingError.__init__(
            self,
            f"Некорректное количество чисел: {invalid_count_value}. "
            f"Ожидается натуральное число (n >= 1)"
        )


class QueueError(HammingError):
    """Исключение для ошибок работы с очередью."""
    pass
