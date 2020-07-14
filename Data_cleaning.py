
import numpy as np

def age(raw_data):
    for ages in (raw_data.age):
        if ages <= 51:
            raw_data['age'] = raw_data.replace(ages, 0)
        if (ages <= 59) and (52 <= ages):
            raw_data['age'] = raw_data.replace(ages, 1)
        if ages <= 77 and (60 <= ages):
            raw_data['age'] = raw_data.replace(ages, 2)

    values, count = np.unique(raw_data['age'], return_counts=True)
    print('age', values, count)