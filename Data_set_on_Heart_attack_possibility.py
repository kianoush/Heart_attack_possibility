"""
About data set
This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to
this date.The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no/less chance of heart attack and 1 = more chance of heart attack

Attribute Information
1) age
2) sex
3) chest pain type (4 values)
4) resting blood pressure
5) serum cholestoral in mg/dl
6)fasting blood sugar > 120 mg/dl(values 0,1)
7) resting electrocardiographic results (values 0,1,2)
8) maximum heart rate achieved
9) exercise induced angina (values 0,1)
10) oldpeak = ST depression induced by exercise relative to rest
11) the slope of the peak exercise ST segment(values 0,1,2)
12) number of major vessels (0-3) colored by flourosopy (values 0,1,2,3,4)
13) thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
14) target: 0= less chance of heart attack 1= more chance of heart attack ---- label

"""

import torch
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


print(os.listdir())

raw_data = pd.read_csv('datasets_heart.csv')

print(np.unique(raw_data.ca))


print('END!')
