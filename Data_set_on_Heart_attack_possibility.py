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
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix
import seaborn as sns
import Data_cleaning

print(os.listdir())

raw_data = pd.read_csv('datasets_heart.csv')
print(raw_data.columns)

for value in raw_data.columns:
    values, count = np.unique(raw_data[value], return_counts=True)
    print(value, values, count)
    print(sum(count))

#sns.pairplot(raw_data)

"""
Divide age to 5 
"""

Data_cleaning.trestbps(raw_data.trestbps)
Data_cleaning.age(raw_data.age)
clean_outlier_data_of_chol = np.where(raw_data.chol == 564)
raw_data = raw_data.drop(clean_outlier_data_of_chol[0][0])
print(raw_data.info())
Data_cleaning.chol(raw_data.chol)
Data_cleaning.thalach(raw_data.thalach)



# box_plot_data = [raw_data['trestbps'], raw_data['thalach']]
# plt.boxplot(box_plot_data, patch_artist=True, labels=['trestbps', 'thalach'])
# plt.show()
#
# box_plot_data = [raw_data['age']]
# plt.boxplot(box_plot_data, patch_artist=True, labels=['age'])
# plt.show()
#
# box_plot_data = [raw_data['chol']]
# plt.boxplot(box_plot_data, patch_artist=True, labels=['chol'])
# plt.show()
#
# box_plot_data = [raw_data['oldpeak']]
# plt.boxplot(box_plot_data, patch_artist=True, labels=['oldpeak'])
# plt.show()
#
# box_plot_data = [raw_data['ca']]
# plt.boxplot(box_plot_data, patch_artist=True, labels=['ca'])
# plt.show()
#
# box_plot_data = [raw_data['sex'], raw_data['cp'], raw_data['fbs'],
#                raw_data['restecg'], raw_data['exang'], raw_data['slope'],
#                raw_data['thal'], raw_data['target']]
#
# plt.boxplot(box_plot_data)
# plt.show()

print('END!')
