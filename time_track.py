from selenium import webdriver as wbd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time_ui import task
from selenium.common import exceptions

#WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH,xpath))
def isAttribute(element,attribute):
    res = False
    value  = ""
    try:
        value = element.get_attribute(attribute)
        if value!=None:
            res = True
    except AttributeError:
        pass

    return res


#Put your email id credentials

email = "clockifytrial@gmail.com"
password  = "Clockify0321"

#put your chrome.exe path
#Check the following link for more information on chrome.exe path :
#https://www.edureka.co/community/3423/exceptions-webdriverexception-chromedriver-executable

chrome_path = 'C:\\Users\\devar\\.wdm\\drivers\\chromedriver\\80.0.3987.106\\win32\\chromedriver.exe'
url = "https://clockify.me/"


#get name from UI
clockify_task = task()

if clockify_task!="":

    driver = wbd.Chrome(chrome_path)
    driver.get(url)
    clockify_task+="\n"
    wait = WebDriverWait(driver,10)

    #click on login
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="newUserHeader"]/li/a'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="identifierId"]'))).send_keys(email)
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="identifierNext"]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="passwordNext"]'))).click()

    #close if any task open
    time.sleep(10)

    #read from file and input
    textbox = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layout-main"]/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/form/input')))
    start_btn = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layout-main"]/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/stopwatch/div[2]/div/button[2]')))
    textbox_value = textbox.get_attribute('value')
    title=""
    if isAttribute(start_btn,'title'):
        title = start_btn.get_attribute('title')

    if title.strip()=="Stop (s)":
        start_btn.click()

    time.sleep(1)
    ignored_exceptions=(exceptions.NoSuchElementException,exceptions.StaleElementReferenceException,)
    textbox= WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layout-main"]/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/form/input')))
    textbox.send_keys(clockify_task)
    start_btn=WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="layout-main"]/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/stopwatch/div[2]/div/button[2]')))
    start_btn.click()

#closing the browser
driver.stop_client()
driver.quit()
