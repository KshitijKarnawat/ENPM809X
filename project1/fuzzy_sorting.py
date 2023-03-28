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
import pandas as pd
import time
from matplotlib import pyplot as plt
from random import randint


def fuzzy_sort(arr, begin, end):
    """
    Returns intervals in a fuzzy sorted manner for the given array of intevals

        Parameters:
            arr (list of lists): The list of intervals that are to be sorted
            begin (int):         The start of the list
            end (int):           The end of the list

        Returns:
            None
    """

    if begin < end:
        q, t = random_partition(arr, begin, end)

        fuzzy_sort(arr, begin, q - 1)
        fuzzy_sort(arr, t + 1, end)


def random_partition(arr, begin, end):
    """
    Chooses a random interval as the pivot.

        Parameters:
            arr (list of lists): The list of intervals that are to be sorted
            begin (int):         The start of the list
            end (int):           The end of the list

        Returns:
            Tuple: The end and start points for the split lists
    """
        
    i = randint(begin, end)
    # swap pivot with last element
    arr[i], arr[end] = arr[end], arr[i]

    return partition(arr, begin, end)


def partition(arr, begin, end):
    """
    Splits the list into two and returns the end and start intervals for the split lists.

        Parameters:
            arr (list of lists): The list of intervals that are to be sorted
            begin (int):         The start of the list
            end (int):           The end of the list

        Returns:
            Tuple: The end and start points for the split lists
    """

    pivot = arr[end]
    q = begin - 1
    t = begin - 1

    for i in range(begin, end):
        if arr[i][1] < pivot[0]:
            t += 1
            q += 1
            arr[t], arr[q] = arr[q], arr[t]

            if t != i:
                arr[i], arr[q] = arr[q], arr[i]
        elif (arr[i][0] <= pivot[1] and pivot[0] <= arr[i][1]):
            t += 1
            arr[t], arr[i] = arr[i], arr[t]

    arr[t + 1], arr[end] = arr[end], arr[t + 1]

    return q + 1, t + 1


def create_intervals(size, df):
    """
    Convert the dataframe into a list of intervals

        Parameters:
            size (int): size of the list
            df (Pandas dataframe): Data read from the `*.txt` file

        Returns:
            List: List of intervals
    """
    arr = []
    for i in range(0,size):
        [a,b] = df[0][i], df[1][i]
        arr.append([a,b])
    return arr


def plot(time_taken):
    """
    Plot the data size vs time taken to sort graph

        Parameter:
            time_taken (list of lists): A list of lists which contains the size of the data and the time taken to execute it.
        
        Returns:
            None
    """
    print(time_taken)
    x = []
    y = []
    for i in time_taken:
        x.append([i[0]])
        y.append([i[1]])
    plt.plot(x,y)


def small_overlap():
    """
    Read the data from the `small_overlap.txt` file and call the fuzzy sorting function on the data. 
    The function calls fuzzy sorting multiple times with different sizes of data and records the time required to sort it.
    It then plots a graph of size vs time taken to sort.
    
        Parameter:
            None

        Returns:
            None
    """

    # Read data from file
    df = pd.read_fwf('small_overlap.txt', header = None)
    time_taken_small = []

    # Size 10
    arr = create_intervals(10, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((10,exec_time))
    print((10,exec_time))

    # Size 100
    arr = create_intervals(100, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((100,exec_time))
    print((100,exec_time))

    # Size 1000
    arr = create_intervals(1000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((1000,exec_time))
    print((1000,exec_time))

    # Size 10000
    arr = create_intervals(10000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((10000,exec_time))
    print((10000,exec_time))

    # Size 100000
    arr = create_intervals(100000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((100000,exec_time))
    print((100000,exec_time))

    # Size 1000000
    arr = create_intervals(1000000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_small.append((1000000,exec_time))
    print((1000000,exec_time))

    # Plot
    plot(time_taken_small)


def all_overlap():
    """
    Read the data from the `all_overlap.txt` file and call the fuzzy sorting function on the data. 
    The function calls fuzzy sorting multiple times with different sizes of data and records the time required to sort it.
    It then plots a graph of size vs time taken to sort.
        
        Parameter:
            None
                    
        Returns:
            None
    """

    # Read data from file
    df = pd.read_fwf('all_overlap.txt', header = None)
    time_taken_all = []

    # Size 10
    arr = create_intervals(10, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((10,exec_time))
    print((10,exec_time))

    # Size 100
    arr = create_intervals(100, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((100,exec_time))
    print((100,exec_time))

    # Size 1000
    arr = create_intervals(1000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((1000,exec_time))
    print((1000,exec_time))

    # Size 10000
    arr = create_intervals(10000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((10000,exec_time))
    print((10000,exec_time))

    # Size 100000
    arr = create_intervals(100000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((100000,exec_time))
    print((100000,exec_time))

    # Size 1000000
    arr = create_intervals(1000000, df)
    begin = time.time()
    fuzzy_sort(arr, 0, len(arr)-1)
    end = time.time()
    exec_time = end - begin
    time_taken_all.append((1000000,exec_time))
    print((1000000,exec_time))

    # Plot
    plot(time_taken_all)


def main():
    
    small_overlap()
    
    all_overlap()

    # Plot the graphs
    plt.legend(["small overlap", "all overlap"])
    plt.show()


if __name__ == "__main__":
    main()
