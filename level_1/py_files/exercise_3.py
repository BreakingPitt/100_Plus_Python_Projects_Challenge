#!/usr/bin/env python
# -*- coding: utf-8 -*-

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). then the program should print the
# dictionary.Suppose the following input is supplied to the program: 8

numbers = int(input())
computed_values = dict()

for number in range(1, numbers + 1):
    computed_values[number] = number * number

print(computed_values)

