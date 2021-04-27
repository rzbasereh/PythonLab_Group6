import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

df.boxplot(column=['ApplicantIncome'], by=['Education'])
plt.show()