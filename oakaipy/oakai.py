# package file including AI tools.

import array
import random


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def get_min(arr):
    mmin = 99999999999
    n = len(arr)
    for i in range(n):
        if arr[i] < mmin:
            mmin = arr[i]
    return mmin


def get_max(arr):
    mmax = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > mmax:
            mmax = arr[i]
    return mmax


def find_resid(arr):
    return


def find_mean(arr):
    n = len(arr)
    i = 0
    dsum = 0;
    while i < n:
        dsum += arr[i]
        i += 1
    return float(float(dsum)/float(n))


def average_change(arr):
    n = len(arr)
    i = 1
    dsum = 0
    while i < n:
        dsum += abs(arr[i] - arr[i-1])
        i += 1
    return float(float(dsum)/float(n))


def predict_next(arr):
    n = len(arr) - 1
    increm = float(find_mean(arr))/float(average_change(arr))
    return round(arr[n] + increm)


def possible_previous(arr):
    n = 0
    increm = float(find_mean(arr)) / float(average_change(arr))
    return arr[0] - round(increm)


def mid_values(arr):
    return


myarr = array.array('i')

size = 10
j = 0;
while j < size:
    myarr.append(random.randint(1, 101))
    j+=1

print('unsorted: '+ str(myarr))
bubblesort(myarr)
print('sorted: '+ str(myarr))
print('minimum value: '+str(get_min(myarr)))
print('maximum value: '+str(get_max(myarr)))
print('mean of set: '+str(find_mean(myarr)))
print('average change: '+str(average_change((myarr))))
print('last value: '+str(myarr[9]))
print('next expected value: '+str(predict_next(myarr)))
print('possible previous value: ' + str(possible_previous(myarr)))
