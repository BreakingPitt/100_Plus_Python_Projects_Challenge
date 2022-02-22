#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

C=50
H=30

def calc(values):
    for value in input_values:
        square_root=math.sqrt((2*C*float(value))/H)
        print square_root

input_values=raw_input("Enter values: ").split(',')
calc(input_values)
