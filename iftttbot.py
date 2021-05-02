from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests, threading,glob,sys
import bs4 as bs
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Invalid input, usage requires: Username Password AppletID")
        exit()

    email = sys.argv[1]
    password = sys.argv[2]
    appletID = sys.argv[3]

    print("Checking if the email and password are correct")

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver",options=options)    
    '''
    make checking window invisible
    '''
    driver.set_window_position(5000, 5000) 
    
    driver.get("https://ifttt.com/login?wp_=1")
    sleep(1)
    driver.find_element_by_id("user_username").send_keys(email)
    sleep(1)
    driver.find_element_by_id("user_password").send_keys(password)
    sleep(1)
    driver.find_element_by_name("commit").click()
    sleep(1)

    expected_url = "https://ifttt.com/home"
    login_success = expected_url == driver.current_url
    print("expected_url = " + expected_url + ", .current_url = " + driver.current_url)
    print("successfull login = " + str(login_success))
    if not(login_success):
        driver.close()
        print("Username / Password combination not valid")
        print("Username: " + email + " Password: " + password)
        exit()

    url = ("https://ifttt.com/applets/" + appletID)
    driver.get(url)
    sleep(2)

    button = driver.find_element_by_link_text('Check now')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    print("Check completed at ", dt_string)

    sleep(5)
    driver.close()
