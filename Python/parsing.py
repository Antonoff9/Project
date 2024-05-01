import time
import json
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

LINK = "https://единый-визовый-центр.рф"

USERS = [
    {'name': "Александра",     'tel': "+70000000000"},
    {'name': "Николай",        'tel': "+70000000000"},
   
]

def wait_find_elenent(driver, xpath, wait=10):
    return WebDriverWait(driver, wait).until( lambda x: x.find_element(By.XPATH, xpath) )

def main():
    with open("web_elements.json", 'r', encoding='utf-8') as web_els_f:
        web_elems = json.load(web_els_f)
    
    for user in USERS:
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 700)
        driver.get(LINK)
        time.sleep(3)
        driver.switch_to.frame( wait_find_elenent(driver, web_elems['main_page']['callback_frame']) )
        time.sleep(1)
        wait_find_elenent(driver, web_elems['main_page']['call_button']).click()
        name_field = wait_find_elenent(driver, web_elems['main_page']['name_field_fr'])
        name_field.send_keys(user['name'])
        tel_field = wait_find_elenent(driver, web_elems['main_page']['tel_field_fr'])
        tel_field.send_keys(user['tel'])
        time.sleep(1)
        wait_find_elenent(driver, web_elems['main_page']['submit_but']).click()
        time.sleep(5)
        try:
            print( driver.find_element(By.XPATH, web_elems['main_page']['accept']).text )
        except Exception as e:
            print(f'ERROR {e}')
        time.sleep(35)
        driver.quit()
    
if __name__ == "__main__":
    main()