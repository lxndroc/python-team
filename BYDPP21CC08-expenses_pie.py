'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #06 (BYDPP21CC06)
1 Mar 2021, 8pm GMT
Host: @kremi
Coach: @alexandros
 
Task
Create an expenses pie chart by month from a corresponding CSV file

Installation Required
> pandas package

Python Code - Initial Effort
As below, being non-optimised, as in the call with minor edits.
'''

import pandas as pd

df = pd.read_csv('data.csv')
print(df)

'''
Input, CSV, file
Month,Food,Transportation
March,$300,$150
April,$250,$150
December,$350,$150

Output
      Month  Food Transportation
0     March  $300           $150
1     April  $250           $150
2  December  $350           $150
'''