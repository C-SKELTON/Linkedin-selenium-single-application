from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")
chrome_driver_path = Service("C:/Users/conno/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3048378073&f_AL=true&f_JT=F&f_TPR=r2592000&geoId=103644278&keywords=sql%20analyst&location=United%20States")
driver.maximize_window()
time.sleep(5)
id_ = os.getenv("LN_Email")
pass_ = os.getenv("LN_Password")

sign_in_btn = driver.find_element(By.LINK_TEXT,'Sign in')
sign_in_btn.click()

login_id = driver.find_element(By.ID, 'username')
login_id.send_keys(id_) #Your Username

password_id = driver.find_element(By.ID, 'password')
password_id.send_keys(pass_) #Your Password

login_btn = driver.find_element(By.CSS_SELECTOR,'.btn__primary--large')
login_btn.click()

#chat_minimize = driver.find_element(By.XPATH, '//*[@id="msg-overlay"]/div[1]/header/div[2]')
chat_minimize = driver.find_element(By.CSS_SELECTOR, '.msg-overlay-bubble-header__details')
chat_minimize.click()
time.sleep(3)

job_container = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[2]/div/div[1]')

#job_container = driver.find_element(By.CSS_SELECTOR, '.job-card-list__entity-lockup')
job_container.click()

time.sleep(2)

#apply_btn = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button')
apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button')
apply_btn.click()
time.sleep(2)
app_next_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button')
app_next_btn.click()
time.sleep(1)
app_review_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]')
app_review_btn.click()

time.sleep(1)
driver.quit()