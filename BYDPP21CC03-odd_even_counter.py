'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #03 (BYDPP21CC03)
8 Feb 2021, 8pm GMT
Host: @PunjabiBagh
Coach: @alexandros

Task Reference
 Gaddis T., Starting Out with Python, Pearson, 2019, 4th global ed.
 p305 Programming Exercise 16

Task
11. Random Number Guessing Game
Odd/Even Counter
In this chapter you saw an example of how to write an algorithm
that determines whether a number is even or odd.
Write a program that generates 100 random numbers,
and keeps a count of how many of those random numbers are even and how many are odd.

Python Code
As below, being non-optimised, as in the call.
'''

import random

def main():
    count_odd_even()

def count_odd_even():
    odd_num_count = 0
    even_num_count = 0
    for i in range(100):
        num = random.randrange(1000)
        num_is_even = num % 2 == 0
        if num_is_even == 0:
            even_num_count += 1
        else:
            odd_num_count += 1
    print(f'Count of odd numbers is {odd_num_count} and count of even numbers is {even_num_count}')

main()