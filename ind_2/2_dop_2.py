#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#генерация пар скобок
def generate(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            generate(count, s + '(', left + 1, right)
        if right < left:
            generate(count, s + ')', left, right + 1)


if __name__ == '__main__':
    print("Введите количество пар скобок: ")
    n = int(input())
    generate(n)