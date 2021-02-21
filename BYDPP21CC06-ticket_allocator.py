'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #06 (BYDPP21CC06)
19 Feb 2021, 8pm GMT
Host: @ssjaseh_3rd
Coach: @alexandros

Task Reference
 Matthes E., Python Crash Course, No Starch Press, 2019, 2nd ed.
 p123 Exercise 7-5
 
Task
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age.
If a person is under the age of 3, the ticket is free;
if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age,
and then tell them the cost of their movie ticket.

Python Code
As below, being non-optimised, as in the call with minor edits.
'''

prompt = "Please let me know your age to get your ticket price:\n"\
 + "Enter age here, or enter value < 3 to quit program."
while True:
    entry = input(prompt)
    if not entry.isdigit():
        print("You have to enter an integer.")
        continue
    age = int(entry)
    if age >= 3 and age <= 12:
        print("The ticket price is $10.")
    elif age > 12:
        print("The ticket price is twelve")
    else:
        print("The program has now ended.")
        break
