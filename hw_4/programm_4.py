"""Задача.
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
"""
from statistics import correlation


def pearson_correlation(num_list_1: [int], num_list_2: [int]) -> float:
    return round(correlation(num_list_1, num_list_2), 2)


if __name__ == "__main__":
    list_1 = [1, 8, 6, 48, 10, 3]
    list_2 = [2, 18, 0, 25, 4, 9]
    print(pearson_correlation(list_1, list_2))
