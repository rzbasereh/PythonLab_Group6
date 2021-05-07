import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))
df = pd.read_csv('train.csv')

ApplicantIncome = df.ApplicantIncome.tolist()
Credit_History = df.Credit_History.tolist()

plt.subplot(121)
plt.plot(Credit_History, ApplicantIncome)

Loan_Status = [1 if item == 'Y' else 0 for item in df.Loan_Status.tolist()]

plt.subplot(122)
plt.plot(Credit_History, Loan_Status)

print(Credit_History)
plt.show()