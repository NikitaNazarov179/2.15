#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Напишите программу, которая будет проходить по файлу с исходным кодом на Python и
искать функции, не снабженные блоком комментариев. Можно принять за аксиому, что
строка, начинающаяся со слова def, следом за которым идет пробел, будет считаться
началом функции. И если функция документирована, предшествующая строчка должна
начинаться со знака #. Перечислите названия всех функций, не снабженных
комментариями, вместе с именем файла и номером строки, с которой начинается
объявление функции. Одно или несколько имен файлов с кодом на языке Python
пользователь должен передать в функцию в качестве аргументов командной строки. Для
файлов, которые не существуют или не могут быть открыты, должны выдаваться
соответствующие предупреждения, после чего должна быть продолжена обработка
остальных файлов."""

from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        print("Нет аргумента(название файлов).")
        quit()

    for fname in argv[1: len(argv)]:
        with open(fname, "r") as fna:
            inf = fna.readlines()

        pred = " "
        count = 1

        for i in inf:
            # Поиск функции без комментария
            if i.startswith("def ") and pred[0] != "#":
                skob = i.index("(")
                funk = i[4: skob]

                print("Название файла: ", fname)
                print("Номер строки: ", count)
                print("Название функции: ", funk)
                print()

            pred = i
            count += 1