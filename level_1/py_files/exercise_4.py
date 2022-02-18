#!/usr/bin/env python
# -*- coding: utf-8 -*-

numbers = input('Type in numbers seperated only by a comma :')

numbers_split = numbers.split(',')
numbers_tuple = tuple(numbers_split)

print(numbers_split)
print(numbers_tuple)
