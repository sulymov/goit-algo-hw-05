from typing import Callable
import re

def generator_numbers(text: str):
    matches = re.findall(r" \d+\.\d+ | \d+ ", text)
    for match in matches:
        number = float(match)
        yield number

def sum_profit(text: str, func: Callable):
    total_income = 0
    for number in func(text):
        total_income += number    
    return total_income

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
