#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

number = int(input())
print(fact(number))
