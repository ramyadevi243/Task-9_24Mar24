import time

# Imported the required webdriver, GeckoDriverManager and Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# Created class called SauceDemo
class SauceDemo:

    # Calling constructor with parameter url
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # Defining a function to maximize window and get specified url
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Defining a method to login the home page of the specified url
    def login(self):
        username = self.driver.find_element("id", "user-name")
        password = self.driver.find_element("id", "password")
        login_button = self.driver.find_element("xpath","//*[@type='submit']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        time.sleep(5)

        login_button.click()

    # Defining a method to get the title of webpage
    def webpage_title(self):
        title = self.driver.title
        print(title)

    # Defining a method to get current url of webpage
    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    # Defining a method to extract the entire content of webpage and
    # save it in a text file
    # and print the content into the console
    def webpage_content(self):
        content = self.driver.find_element("tag name","body").text
        print(content)

        with open("Webpage_task_11.txt", "w", encoding="utf-8")as file:
            file.write(content)

# Executing the main method
if __name__ == "__main__":
    # Passing the value to the url
    url = "https://www.saucedemo.com/"
    # Creating an object for the class SauceDemo
    sauce = SauceDemo(url)

    # Calling all the methods
    sauce.start()
    sauce.login()
    sauce.webpage_title()
    sauce.current_url()
    sauce.webpage_content()