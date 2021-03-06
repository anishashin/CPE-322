import numpy as np
import matplotlib.pyplot as plt
import pdb
from pandas import *
data = read_csv('train.csv')
cols = data.columns
print('Data Columns:')
print(cols)
survivors = data.groupby('Sex').Survived.mean()
print('Survived:')
print(survivors)
###MODIFIED CODE###
survivors = data.groupby('Pclass').Survived.mean()
print('Survived:')
print(survivors)
###################
plt.hist(data.Pclass, bins=[1,2,3,4], align='left', rwidth=0.5)
plt.xticks([0,1,2,3,4])
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.show()
###MODIFIED CODE###
plt.hist(data.Sex, bins=["male","female",""], align='left', rwidth=0.5)
plt.xticks([-1,0,1,2])
plt.xlabel('Sex')
plt.ylabel('Number of Passengers')
plt.show()
###################
