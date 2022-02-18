#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = int(input())
computed_values = dict()

for number in range(1, numbers + 1):
    computed_values[number] = number * number

print(computed_values)

