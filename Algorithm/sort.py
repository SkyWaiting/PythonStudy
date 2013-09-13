__author__ = 'guorui'
# -*- coding:utf-8 -*-
# 测试各种排序算法
# http://my.oschina.net/memorybox/blog/69709

# 选择排序
def select_sort(sort_array):
    for i,elem in enumerate(sort_array):
        for j,elem in enumerate(sort_array[i:]):
            if sort_array[i] > sort_array[j+i]:
                #交换
                sort_array[i],sort_array[j+i] = sort_array[j+i],sort_array[i]


# 冒泡排序
def bubble_sort(sort_array):
    for i,elem in enumerate(sort_array):
        for j,elem in enumerate(sort_array[:len(sort_array)-i-1]):
            if sort_array[j] > sort_array[j+1]:
                sort_array[j],sort_array[j+1] = sort_array[j+1],sort_array[j]

# 插入排序
def insert_sort(sort_array):
    for i,elm in enumerate(sort_array):
        for j,elm in enumerate(sort_array[:i]):
            if sort_array[j] > sort_array[i]:
                sort_array.insert(j,sort_array[i])
                del sort_array[i+1]
