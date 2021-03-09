'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #10 (BYDPP21CC10)
8 Mar 2021, 8pm GMT
Host: @kremi
Coach: @alexandros
 
Task
Create an expenses pie chart by month from a corresponding CSV file

Installation Required
> matplotlib package
> pandas package

Python Code - 2nd Effort
As below, being non-optimised, as in the call with minor edits.
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
#print(df)

expenses = df['Food'] + df['Transportation'] + df['rent']

plt.pie(expenses, labels=('March', 'April', 'December'), autopct='%1.1f%%')
plt.title('Monthly Expenses')
plt.show()

'''
Input - data.csv
Month,Food,Transportation,rent
March,300,150,800
April,250,150,800
December,350,150,800
'''
