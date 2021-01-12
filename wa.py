
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import sys


def login():

    wa_login_wait_el = '//span[@data-testid="chat"][@data-icon="chat"]'

    driver.implicitly_wait(10)

    # wait for whatsapp login
    wait_for_login = True
    MAX_LOGIN_CHECK=10
    while wait_for_login:
        try:
            MAX_LOGIN_CHECK +=1
            driver.find_element_by_xpath(wa_login_wait_el)
        except:
            if MAX_LOGIN_CHECK > 10:
                print("either network is slow or something has changed on whatsapp home page")
                sys.exit(0)
            pass
        else:
            print("logged in")
            wait_for_login = False


def send_msg(name, message):
    contact_search_input = '//div[@class="_1awRl copyable-text selectable-text"][@dir="ltr"][@data-tab="3"]'
    #select name
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, contact_search_input)))

    input_box.click()
    input_box.send_keys(name + Keys.ENTER)
    #select msg input box
    msg_input = '//div[@class="_1awRl copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, msg_input)))
    input_box.click()
    #send msg
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)


csv_path = "/home/rahul/Downloads/wa_driver/test.csv"

# Replace below path with the absolute path
# to chromedriver in your computer
webdriver_path = "/home/rahul/Downloads/wa_driver/chromedriver"
driver = webdriver.Chrome(webdriver_path)
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 600)

with open(csv_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            name=row[0]
            message=row[1]
            print(f"sending \"{message}\" to \"{name}\"")
            send_msg(name,message)
            line_count += 1
driver.close()
print("Done!!!!")
