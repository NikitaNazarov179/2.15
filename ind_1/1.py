#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open("ind_1.txt", "r") as fileptr:
        sentences = fileptr.readlines()

    for sentence in sentences:
        if "?" in sentence or "!" in sentence:
            print(sentence)