import sys
from pathlib import Path

# Функція для парсингу логів рядку
def parse_log_line(line: str) -> dict:
    
    # Створюємо порожній словник 
    dict_log = {}
    
    # Розбиваємо логи за пробілами в якості розділювачів. Максимальний індекс елементу 3. Туди записується залишок рядка
    divided_log = line.split(" ", 3)
    dict_log["date"] = divided_log[0].strip()
    dict_log["time"] = divided_log[1].strip()
    dict_log["level"] = divided_log[2].strip()
    dict_log["info"] = divided_log[3].strip()

    # Функція повертає словник, де ключі - компоненти логу (дата, час рівень, інформація)
    return dict_log


# Функція для завантаження логів з файлу. Приймає шлях до логфайла та рівень логування (необов'язковий аргумент)
def load_logs(file_path: str) -> list:
    
    # Якщо шлях до файлу прописаний вірно і файл існує
    try:
        with open(file_path, "r", encoding="utf-8") as fh:

            # Створюється порожній список та заповнюється словниками після парсингу рядків
            logs = []
            for el in fh.readlines():
                logs.append(parse_log_line(el.strip()))

            # Функція повертає список, де кожний елемент - словник, який містить інформацію по логу
            return logs
    
    # Обробка винятку існування файла
    except FileNotFoundError:
        logs = f"\n Файл за шляхом {file_path} відсутній \n"
        return logs


# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:

    all_levels = ["error", "info", "debug", "warning"]
    # Якщо в командному рядку був правильно введений рівень логування, то формуємо список логів за рівнем 
    result = any(level_from_all_levels == level.lower() for level_from_all_levels in all_levels)

    if result:

        # Проходимося по списку логов та в кожному словнику шукаємо співпадіння по рівню лога 
        logs_by_level = [f"{log["date"]} {log["time"]} - {log["info"]}" for log in logs if level.upper() == log["level"]]

        # Функція повертає відфільтрований список логів за рівнем, введеним з командного рядка 
        return logs_by_level   
   
    # Якщо рівень логування введений не вірно, повертаємо повідомлення про помилку
    else:
        return f"Рівень логування {level.upper()} не існує. Спробуйте знову! Існуючі рівні INFO, ERROR, DEBUG, WARNING \n"


# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    # Створюємо порожній словник з підрахунком логів за рівнями
    counts = {}
    # print(logs, type(logs))
    # Проходимося по списку зі словниками logs та наповнюємо counts елементами збільшуючи значення на 1 при кожному співпадінні
    for log in logs:
        if log["level"] in counts:
            counts[log["level"]] += 1
        else:
            counts[log["level"]] = 1

    # Функція повертає словник, де ключі - рівні логів, значення - їх кількість повторень
    return counts


# Функція для виводу результатів у вигляді таблиці. Вона приймає результати виконання функції count_logs_by_level
def display_log_counts(counts: dict):

    print("\t")
    print("-"*28)
    print("Рівень логування | Кількість")
    print("-"*28)

    for level, count in counts.items():
        spaces = 15 - len(level)
        print(level, " " * spaces, "|", count)
    print("-"*28, "\n")


# ************** ВИКОНАННЯ ПРОГРАМИ  ***********

# Спочатку завантажуємо логи з файлу. В результаті маємо список словників з інфо по кожному логу
logs = load_logs(sys.argv[1])
# Якщо було повідодмлення про помилку в шляху до файла, виводимо повідомлення на екран і на цьому кінець
if type(logs) is str:
    print(logs)
# Якщо ми отримали список, тоді програма працює далі  
elif type(logs) is list:

    # Рахуємо записи за рівнем логування
    counts = count_logs_by_level(logs)

    # Виводимо результати на екран
    display_log_counts(counts)

    # Перевіряємо існування необов'язкового аргумента. Якщо він існує - проводимо фільтрацію логів за рівнем
    if len(sys.argv) == 3:

        # Проводимо фільтрацію логів за рівнем 
        logs_by_level = filter_logs_by_level(logs, sys.argv[2])
        
        # Якщо повертається список, то виводимо його на екран циклом
        if type(logs_by_level) is list:

            # Виводимо результати фільтрації на екран
            print(f"Деталі логів для рівня {sys.argv[2].upper()}:")

            for log in logs_by_level:
                print(log)
            print("\t")

        # В разі, якщо функція видала помилку - виводимо повідомлення про помилку
        elif type(logs_by_level) is str:
            print(logs_by_level)