from selenium import webdriver

#make sure gecko driver is in the usr/bin folder

browser = webdriver.Firefox()
browser.get('https://www.reddit.com/')