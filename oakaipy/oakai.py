# package file including AI tools.

import array
import random


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
        i+=1
    return float(float(dsum)/float(n))


def predict_next(arr):
    n = len(arr) - 1
    increm = float(find_mean(arr))/float(average_change(arr))
    return arr[n] * increm


def possible_previous(arr):
    return


def mid_values(arr):
    return


myarr = array.array('i')

size = 10
j = 0;
while j < size:
    myarr.append(random.randint(1, 101))
    j+=1

k = 0
while k < size:
    print(myarr[k])
    k += 1

print(find_mean(myarr))
print(average_change((myarr)))
print(myarr[9])
print(predict_next(myarr))
