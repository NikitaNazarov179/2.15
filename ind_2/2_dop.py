#!/usr/bin/env python3
# -*- coding: utf-8 -*

def best_singer(**kwargs):
    st = "-" * 45
    print("Альбомы инстасамки: \n")
    print(st)
    for field, goddess in kwargs.items():
        print(f"{field}:", " "*(5-len(field)), goddess)
        print(st)


if __name__ == "__main__":
    best_singer(
        QUEEN_OF_RAP = ["LIPSI HA", "MONEYKENLOVE", "RARARA"],
        MONEYDEALER = ["JUICY", "FACETIME", "И ЧТОЭ"],
        MAMACITA = ["ALL INCLUSIVE", "CASINO", "JACKPOT"],
        BORN_TO_FLEX = ["SAY HELLO", "ЧЁ ПО КАЙФУ", "HOLA"]
    )