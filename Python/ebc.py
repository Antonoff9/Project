import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

# driver = webdriver.Firefox(executable_path='C:\\Users\\ASUS\\Desktop\\geckodriver.exe')
# driver.get('http://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('FirefoxDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()

# link = "https://xn-----elcahffngcif9bjk1b7a3e8dh.xn--p1ai/"
link = "единый-визовый-центр.рф"
options = ChromeOptions()
options.binary_location = "C:\\chromedriver\\chromedriver.exe"
browser = webdriver.Chrome(options=options)
browser.get(link)

input("...")
  
#ввод номера
search_string = browser.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div[1]/div[1]/label/input")
search_string.send_keys("+79189999999")
