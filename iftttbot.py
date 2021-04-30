from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests, threading,glob,sys
import bs4 as bs
from selenium.webdriver.common.action_chains import ActionChains


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Invalid input, usage requires: Username Password AppletID")
        exit()

    email = sys.argv[1]
    password = sys.argv[2]
    appletID = sys.argv[3]

    print("Checking if the email and password are correct")
    options = Options()
    # options.add_argument("--incognito")
    # options.add_argument("--headless")
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    '''
    make checking window invisible
    '''
    #browser.set_window_position(5000, 5000) 
    
    browser.get("https://ifttt.com/login?wp_=1")
    sleep(1)
    browser.find_element_by_id("user_username").send_keys(email)
    sleep(1)
    browser.find_element_by_id("user_password").send_keys(password)
    sleep(1)
    browser.find_element_by_name("commit").click()
    sleep(1)

    expected_url = "https://ifttt.com/home"
    login_success = expected_url == browser.current_url
    print("expected_url = " + expected_url + ", browser.current_url = " + browser.current_url)
    print("successfull login = " + str(login_success))
    if not(login_success):
        browser.close()
        print("Username / Password combination not valid")
        print("Username: " + email + " Password: " + password)
        exit()

    url = ("https://ifttt.com/applets/" + appletID)
    browser.get(url)
    sleep(2)

    button = browser.find_element_by_link_text('Check now')
    browser.implicitly_wait(10)
    ActionChains(browser).move_to_element(button).click(button).perform()
    
    sleep(4)
    browser.close()
