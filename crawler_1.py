from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

url = input('Entering url')
ticnum = input('Entering ticket number')
ticlist = 1

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
chains = ActionChains(driver)
driver.get(url)

def grab_ticket:
    while True:
        if check_exists_by_xpath('/html/body/div[55]/div[1]/div[3]/div/div/div/div[2]/div[2]/ul[3]/li/a') == True:
            ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/ul[3]/li/a')
            ele.click()
            if driver.current_url != url:
                chk = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[3]/div')
                chk.click()
                select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select'))
                select.select_by_visible_text(ticnum)
            else:
                ticlist += 1
                continue

def refresh_ticket:
    while True:
        if check_exists_by_xpath('/html/body/div[55]/div[1]/div[3]/div/div/div/div[2]/div[2]/ul[3]/li/a') == True:
            while True:
                
            ele = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/ul[3]/li/a')
            ele.click()
            if driver.current_url != url:
                chk = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[3]/div')
                chk.click()
                select = Select(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/div/div/div/form/div[1]/table/tbody/tr/td[2]/select'))
                select.select_by_visible_text(ticnum)
            else:

        else:
            driver.refresh()
            print('NoSuchElement')





time.sleep(5)

