'Automate the browser with Selenium'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(
    'c:/Users/amirb/Desktop/amazon_selenium/chromedriver.exe')
driver.get('https://www.amazon.com')
driver.maximize_window()
time.sleep(2)

menu_btn = driver.find_element_by_id('nav-hamburger-menu')
menu_btn.click()
time.sleep(1)
login_btn = driver.find_element_by_id('hmenu-customer-name')
login_btn.click()
time.sleep(4)

username_field = driver.find_element_by_id('ap_email')
username_field.send_keys('bekdevelopment@gmail.com')
username_field.send_keys(Keys.RETURN)
time.sleep(4)
password_field = driver.find_element_by_id('ap_password')
with open('password.txt', 'r') as x:
    password = x.read()
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
print('You are logged in!')
time.sleep(4)

search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Spiderman Statue')
search_loop = driver.find_element_by_class_name('nav-right')
search_loop.click()
print('The search was made succesfully!')
