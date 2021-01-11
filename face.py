from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.facebook.com")

USERNAME = "<<username>>"
PASSWORD = "<<password>>"
user_name_box = driver.find_element_by_id("email")
user_name_box.send_keys(USERNAME)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(PASSWORD)

login_box = driver.find_element_by_id("u_0_b")
login_box.click()
print("Login feito com sucesso!!!")
time.sleep(3)

driver.get("https://www.facebook.com/events/birthdays")
time.sleep(10)

birtbirthday_boxes = driver.find_elements_by_xpath('//*[@class="notranslate _5rpu"]')
count = 0
for els in birtbirthday_boxes:
    try:
        count += 1
        els.send_keys("<<frase de aniversário que você deseja>>")
        time.sleep(2)
        els.send_keys(Keys.ENTER)
        print("Postado para " + str(count))
    except:
        print("Não foi possível postar")

print("Concluído ;)")
time.sleep(2)
driver.close()

