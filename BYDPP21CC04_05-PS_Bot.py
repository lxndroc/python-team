'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #05 (BYDPP21CC05)
15 Feb 2021, 8pm GMT
Host: @Bertan
Coach: @alexandros

Task
Write a bot trying to order a product, which is not in stock and limited.
When the product becomes available, the bot is ordering it automatically.
This is useful for limited stuff, e.g. PS5, Xbox, shoes, Graphics cards.
If the product is unavailable, the bot presses F5 to refresh the page and checks again.
When the product is available, the bot is ordering it by clicking the button
that adds the product to the cart, auto-filling the requested details, and performing checkout.

Installations Required
> selenium package
> keyboard package
> Selenium WebDriver for Chrome
> Google Chrome

Python Code - 2nd Effort
As below, being non-optimised, as in the call with minor edits.
'''

from selenium import webdriver
import keyboard
from time import sleep

class PS_Bot:

    def __init__(self):
        self.mail = input("Enter your email address: ")
        # Test order is a random link that I chose from the website which is in stock. The reason is checking the source codes of addtocartButton
        urlTest = 'https://www.smythstoys.com/uk/en-gb/toys/fashion-and-dolls/soft-toys/brown-bear-plush-100cm/p/168724'

        # The actual link is a PlayStation 5 which is not in stock.
        url = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'

        # We have to install webdriver for Chrome and I just put the path of the driver.
        self.driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")

        # This code is opening the url
        self.driver.get(urlTest)
        self.availabilitycheck()

    def availabilitycheck(self):
        # I defined button as Add to Cart button
        while True:
            try:
                cookies = self.driver.find_element_by_xpath('//*[@id="cookieLoad"]/div/div/div[1]/div[4]/div[1]/button')
                cookies.click()
                sleep(2)
                button = self.driver.find_element_by_xpath('//*[@id="addToCartButton"]')
                button.click()
                sleep(1)
                self.driver.get('https://www.smythstoys.com/uk/en-gb/cart')
                sleep(1)
                checkout = self.driver.find_element_by_xpath('//*[@id="checkoutOnCart"]')
                checkout.click()
                sleep(2)
                email = self.driver.find_element_by_xpath('//*[@id="guest.email"]')
                email.send_keys(self.mail)
                email_repeat = self.driver.find_element_by_xpath('//*[@id="guest.confirmEmail"]')
                email_repeat.send_keys(self.mail)
                checkout_order = self.driver.find_element_by_xpath('//*[@id="confirmEmailGuestForm"]/div[1]/div[2]/div/div[2]/div/button')
                checkout_order.click()

                input()
                break
            except:
                print("Button not found")
                sleep(1)
                keyboard.press_and_release('f5')
                sleep(2)

PS_Bot()
