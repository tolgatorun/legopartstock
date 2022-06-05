from typing import final
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

ID_ARRAY = ['6329624/74085','6360199/77101']

driver.get("https://www.lego.com/en-ca/page/static/pick-a-brick?query")
driver.implicitly_wait(10)

popUp = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div/button')
popUp.click()

cookies = driver.find_element(By.XPATH, '/html/body/div[5]/div/aside/div/div/div[3]/div[1]/button[2]')
cookies.click()

outofStockButton = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div/div/div[3]/div[2]/div/div/label')
outofStockButton.click()
searchBar = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div/div/div[1]/div[1]/form/div/input')
searchBar.send_keys(ID_ARRAY[1])
searchButton = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div[1]/div/div/div[1]/div[1]/form/button')
searchButton.click()

if len(driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div[2]/div/ul/li/div/div[2]/div/button')) != 0:
    stockCheck = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div[2]/div/ul/li/div/div[2]/div/button')
else:
    stockCheck = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div[2]/div/ul/li/div/div[2]/div/div')
price = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div[2]/div/ul/li/div/div[1]/span/span')

output = ['Stock', price.text]

if stockCheck.text == 'PICK':
    output[0] = 'Available'
else:
    output[0] = 'Out of stock'
print(output)
