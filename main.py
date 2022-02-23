#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import time

#
array = []
for _ in range(1000):
    array.append(randint(1, 100))

ST_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if(array[min_index] > array[j]):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


END_T = time.time()

print('선택 정렬 시간: ', END_T -ST_time)

######################################################
array = []
for _ in range(1000):
    array.append(randint(1, 100))

ST_T=time.time()

array.sort()

END_T = time.time()

print('기본정렬 시간:', END_T - ST_T)