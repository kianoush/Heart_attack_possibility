import pandas as pd
import numpy as np




def clean_trestbps(x):
    for item in (x):
        if item <= 120:
            x = x.replace(item, 0)
        if (121 <= item) and (item <= 138):
            x = x.replace(item, 1)
        if (139 <= item)and (item <= 200):
            x = x.replace(item, 2)
    values, count = np.unique(x, return_counts=True)
    print('trestbps', values, count)
    return




def bage(x):
    for ages in (x):
        if ages <= 51:
            x = x.replace(ages, 0)
        if (52 <= ages) and (ages <= 59):
            x = x.replace(ages, 1)
        if (60 <= ages) and (ages <= 77):
            x = x.replace(ages, 2)

    values, count = np.unique(x, return_counts=True)
    print('age', values, count)
    return
