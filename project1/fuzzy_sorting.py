#!/usr/bin/env python3

"""
 * @copyright Copyright (c) 2023
 * @file ariac_competition.cpp
 * @author Kshitij Karnawat (kshitij@umd.edu)
 * @brief Implementation of Fuzzy Sorting of Intervals. (Cormen 7-6)
 * @version 0.1
 * @date 2023-03-27
 * 
 * 
"""

# import libraries
import random
import copy
import pandas as pd
import time
from matplotlib import pyplot as plt
import sys

"""
* @brief
*
* @param
* @param
* @param
*
* @returns
"""
def partition(arr, p, r):
    # choose random pivot
    pivot = random.randint(p, r) 

    #swap pivot with last element
    arr[pivot], arr[r] = arr[r], arr[pivot]
    intersection = copy.deepcopy(arr[r])
    
    for i in range(p, r):
        if intersection[0] <= arr[i][1] and arr[i][1] <= intersection[0]:
            if arr[i][0] > intersection[0]:
                intersection[0] = arr[i][0]
            if arr[i][1] < intersection[1]:
                intersection[1] = arr[i][1]

    s = p
    for i in range(p, r):
        if arr[i][1] < intersection[0]:
            arr[i], arr[s] = arr[s], arr[i]
            s += 1

    arr[r], arr[s] = arr[s], arr[r]


    t = s + 1
    while t <= i:
        if arr[i][0] <= intersection[1] and intersection[1] <= arr[i][0]:
            arr[t], arr[i] = arr[i], arr[t]
            t += 1
        else:
            i -= 1

    return (s, t)

"""
* @brief
*
* @param
* @param
* @param
"""
def fuzzy_sort(arr, p, r):
    if (p < r):
        pivot = partition(arr, p, r)
        fuzzy_sort(arr, p, pivot[0])
        fuzzy_sort(arr, pivot[1], r)


def create_intervals(size, df):
    arr = []
    for i in range(0,size):
        [a,b] = df[0][i], df[1][i]
        arr.append([a,b])
    return arr

def small_overlap():
    df = pd.read_fwf('small_overlap.txt', header = None)
    time_taken_small = []

    arr = create_intervals(10, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((10,exec_time))
    print((10,exec_time))

    arr = create_intervals(100, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((100,exec_time))
    print((100,exec_time))

    arr = create_intervals(1000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((1000,exec_time))
    print((1000,exec_time))

    arr = create_intervals(10000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((10000,exec_time))
    print((10000,exec_time))

    arr = create_intervals(100000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((100000,exec_time))
    print((100000,exec_time))

    arr = create_intervals(1000000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((1000000,exec_time))
    print((1000000,exec_time))

    print(time_taken_small)
    x = []
    y = []
    for i in time_taken_small:
        x.append([i[0]])
        y.append([i[1]])
    plt.plot(x,y)
    plt.show()


def all_overlap():
    df = pd.read_fwf('all_overlap.txt', header = None)
    time_taken_all = []

    arr = create_intervals(10, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((10,exec_time))
    print((10,exec_time))

    arr = create_intervals(100, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((100,exec_time))
    print((100,exec_time))

    arr = create_intervals(1000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((1000,exec_time))
    print((1000,exec_time))

    arr = create_intervals(10000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((10000,exec_time))
    print((10000,exec_time))

    # arr = create_intervals(100000, df)
    # begin = time.time()
    # fuzzy_sort(arr, 0, len(arr)-1)
    # end = time.time()
    # exec_time = end - begin
    # time_taken_all.append((100000,exec_time))
    # print((100000,exec_time))

    # arr = create_intervals(1000000, df)
    # begin = time.time()
    # fuzzy_sort(arr, 0, len(arr)-1)
    # end = time.time()
    # exec_time = end - begin
    # time_taken_all.append((1000000,exec_time))
    # print((1000000,exec_time))

    print(time_taken_all)
    x = []
    y = []
    for i in time_taken_all:
        x.append([i[0]])
        y.append([i[1]])
    plt.plot(x,y)
    plt.show()


def main():
    # sys.setrecursionlimit(100000000)
    # small_overlap()
    all_overlap()
    
if __name__ == "__main__":
    main()