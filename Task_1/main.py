# Функція кешування 
def caching_fibonacci():
    # Створюємо порожній словник для збереження кешованих значень
    cache = {}

    # Функція для обчислення n-ного ряду чисел Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        else:
            # Обчислення n-ного числа Фібоначчі, якщо воно відрізнеяється від 0 та 1 та відсутнє в кеші 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
