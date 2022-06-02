from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

ID_ARRAY = ['6331932/7109']
driver.get("https://www.lego.com/en-ca/page/static/pick-a-brick?query")
driver.implicitly_wait(15)
popUp = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div/button')
popUp.click()
cookies = driver.find_element(By.XPATH, '/html/body/div[5]/div/aside/div/div/div[3]/div[1]/button[2]')
cookies.click()
