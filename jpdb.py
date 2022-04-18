from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from py_console import console
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions 


browser = webdriver.Firefox(executable_path="./geckodriver") # Create a Firefox browser instance

url = "https://jpdb.io/login"

browser.get(url)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/form[2]/div[1]/input[1]"))).send_keys(input("username: ")) # enter username
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/form[2]/div[1]/input[2]"))).send_keys(input("password: ")) # enter password 
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/form[2]/input"))).send_keys(Keys.RETURN)
browser.implicitly_wait(2)
time.sleep(1)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/a"))).click()
browser.implicitly_wait(2)
time.sleep(1)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/a"))).click()

# button xpath: "/html/body/div[2]/div[8]/div[{i}]/div[2]/div[1]/div/details/summary"
for i in range(61):
    for i in range(52):
        try: 
            if browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[8]/div[{i}]").get_attribute("class") == "entry new":
                console.info(browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[8]/div[{i}]").text)
                browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[8]/div[{i}]/div[2]/div[1]/div/details/summary").send_keys(Keys.RETURN)
                try:
                    browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[8]/div[{i}]/div[2]/div[1]/div/details/div/ul/li[1]/form/input[4]").send_keys(Keys.RETURN)
                except selenium.common.exceptions.ElementNotInteractableException:
                    console.warn("button error")
                    pass
        except selenium.common.exceptions.NoSuchElementException:
            pass
    if (browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[9]/a").text == "Next page"):
        browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[9]/a").send_keys(Keys.RETURN)
    elif (browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[9]/a[2]").text == "Next page"):
        browser.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[9]/a[2]").send_keys(Keys.RETURN)
    else:
        console.error("tf")
        


input()
browser.close()