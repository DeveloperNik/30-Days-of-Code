#!/bin/python3

import math
import os
import random
import re
import sys


def count(num):
    count = 0

    while (num != 0):
        num = (num & (num << 1))
        count = count+1

    return count


if __name__ == '__main__':
    n = int(input())
    print(count(n))
