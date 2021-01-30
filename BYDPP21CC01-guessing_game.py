'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team

BYDPP 2021 Coaching Call #01 (BYDPP21CC01) +
25 Jan 2021, 8pm GMT
Host: @PunjabiBagh
Coach: @alexandros

Task Reference
 Gaddis T., Starting Out with Python, Pearson, 2019, 2nd ed.
 p237 Programming Exercise 11

Task
11. Random Number Guessing Game
Write a program that generates a random number in the range of 1 through 100
and asks the user to guess what the number is.
If the user’s guess is higher than the random number,
the program should display "Too high, try again."
If the user’s guess is lower than the random number,
the program should display "Too low, try again."
If the user guesses the number,
the application should congratulate the user
and then generate a new random number so the game can start over.
Optional Enhancement: Enhance the game so it keeps count
of the number of guesses that the user makes.
When the user correctly guesses the random number,
the program should display the number of guesses.

Python Code
As below, being non-optimised, as in the call.
'''

import random

def main():
    num = random.randrange(1,101)
    while True:
        guess(num)

def guess(n):
    attempt = int(input('Guess the number: '))
    a = 0
    while True:
        a += 1
        if attempt > n:
            attempt = int(input('Too high! Try again: '))
        elif attempt < n:
            attempt = int(input('Too low! Try again: '))
        else:
            print('Great! You cracked it in',a,'attempts')
            return True
main()
#Happened over class thanks to Alexandros!