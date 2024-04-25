numerator, denominator = int(input()), int(input())
def changed_div(numerator, denominator):
    try:
        # Вычисляем отношение делителя к частному
        return numerator / denominator
    except ZeroDivisionError:
        # Возвращаем делитель, если делимое равно нулю
        return denominator

print(changed_div(numerator, denominator))
