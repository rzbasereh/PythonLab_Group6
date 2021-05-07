import pandas as pd
import matplotlib.pyplot as plt

n_bins = 50

df = pd.read_csv('train.csv')

ApplicantIncome = df.ApplicantIncome.tolist()
print(ApplicantIncome)

plt.hist(ApplicantIncome, bins = n_bins)
plt.show()
