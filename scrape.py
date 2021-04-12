from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def read_last_in_message():
        """
        Reading the last message that you got in from the chatter
        """
        for messages in driver.find_elements_by_xpath(
                "//div[contains(@class,'message-in')]"):
            try:
                message = ""
                emojis = []

                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']")

                message = message_container.find_element_by_xpath(
                    ".//span[contains(@class,'selectable-text copyable-text')]"
                ).text
                
                for emoji in message_container.find_elements_by_xpath(
                        ".//img[contains(@class,'selectable-text copyable-text')]"
                ):
                    emojis.append(emoji.get_attribute("data-plain-text"))

            except NoSuchElementException:  # In case there are only emojis in the message
                try:
                    message = ""
                    emojis = []
                    message_container = messages.find_element_by_xpath(
                        ".//div[contains(@class,'copyable-text')]")

                    for emoji in message_container.find_elements_by_xpath(
                            ".//img[contains(@class,'selectable-text copyable-text')]"
                    ):
                        emojis.append(emoji.get_attribute("data-plain-text"))
                except NoSuchElementException:
                    pass

        return message, emojis

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')
sleep(25)
print("page ready")
last_in_message, emojis = read_last_in_message()

if(len(last_in_message)>0):
    print(last_in_message)
if(len(emojis)>0):
    print(emojis)
printed_msg=last_in_message

while(True):
    last_in_message, emojis = read_last_in_message()
    if(printed_msg!=last_in_message):
        if(len(last_in_message)>0):
            print(last_in_message)
        if(len(emojis)>0):
            print(emojis)
        printed_msg=last_in_message

