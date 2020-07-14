import pandas as pd
import numpy as np




def trestbps(x):
    for item in (x):
        if item <= 120:
            x = x.replace(item, 0)
        if (121 <= item) and (item <= 138):
            x = x.replace(item, 1)
        if (139 <= item) and (item <= 200):
            x = x.replace(item, 2)
    values, count = np.unique(x, return_counts=True)
    #print('trestbps', values, count)
    return x



def age(x):
    for ages in (x):
        if ages <= 51:
            x = x.replace(ages, 0)
        if (52 <= ages) and (ages <= 59):
            x = x.replace(ages, 1)
        if (60 <= ages) and (ages <= 77):
            x = x.replace(ages, 2)

    values, count = np.unique(x, return_counts=True)
    #print('age', values, count)
    return x



def chol(x):

    for item in (x):
        if item <= 220:
            x = x.replace(item, 0)
        if (221 <= item) and (item<= 260):
            x = x.replace(item, 1)
        if (261 <= item) and (item <= 417):
            x = x.replace(item, 2)

    values, count = np.unique(x, return_counts=True)
    #print('chol', values, count)
    return x


def thalach(x):
    for item in (x):
        if item <= 142:
            x = x.replace(item, 0)
        if (143 <= item) and (item<= 161):
            x = x.replace(item, 1)
        if (162 <= item) and (item <= 202):
            x = x.replace(item, 2)

    values, count = np.unique(x, return_counts=True)
    #print('thalach', values, count)
    return x


def oldpeak(x):
    for item in (x):
        if item == 0:
            x = x.replace(item, 0)
        if (0.1 <= item) and (item <= 1.3):
            x = x.replace(item, 1)
        if (1.4 <= item) and (item <= 6.2):
            x = x.replace(item, 2)

    values, count = np.unique(x, return_counts=True)
    #print('oldpeak', values, count)
    return x