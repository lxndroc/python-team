'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #04 (BYDPP21CC04)
12 Feb 2021, 8pm GMT
Host: @Bertan
Coach: @alexandros

Task
Write a bot trying to order a product, which is not in stock and limited.
When the product becomes available, the bot is ordering it automatically.
This is useful for limited stuff, e.g. PS5, Xbox, shoes, Graphics cards.
If the product is unavailable, the bot presses F5 to refresh the page and checks again.
When the product is available, the bot orders it by clicking the button
that adds the product to the cart.

Installations Required
> selenium package
> keyboard package
> Selenium WebDriver for Chrome
> Google Chrome

Python Code - Initial Effort
As below, being non-optimised, as in the call.
'''

from selenium import webdriver
import keyboard
from time import sleep

class PS_Bot:

    def __init__(self):
        # Test order is a random link that I chose from the website which is in stock. The reason is checking the source codes of addtocartButton
        urlTest = 'https://www.smythstoys.com/uk/en-gb/toys/fashion-and-dolls/soft-toys/brown-bear-plush-100cm/p/168724'

        # The actual link is a PlayStation 5 which is not in stock.
        url = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'
        # We have to install webdriver for Chrome and I just put the path of the driver.
        self.driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

        # This code is opening the url
        self.driver.get(urlTest)
        self.availability_check()

    def availability_check(self):
        # I defined button as Add to Cart button
        while True:
            try:
                button = self.driver.find_element_by_xpath('/html/body/div[7]/section/div/div/div[2]/div[1]/div[5]/div/div/div/div[2]/form/button')
                button.click()
                break
            #if the button is unavailable, refresh the page and check it again.
            except:
                print("Button not found")
                sleep(1)
                keyboard.press_and_release('f5')
                sleep(2)

PS_Bot()