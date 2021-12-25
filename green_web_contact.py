from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

webdriver = "drivers/chromedriver"

driver = Chrome(webdriver)

pages = 10
def run():
    url = "https://www.greenweb.ir/"
    driver.get(url)
r = run()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu-header_3-1702"]/a'))).click()
sleep(2)
txt_name = driver.find_element(By.NAME, 'your-name')
txt_name.send_keys('Ehsan')


txt_name = driver.find_element(By.NAME, 'your-subject')
txt_name.send_keys('Test to crawl your site!')
txt_name = driver.find_element(By.NAME, 'your-message')
txt_name.send_keys("Hey guys! I'm crawling your web site, Have fun!",)

select = Select(driver.find_element(By.NAME, 'menu-178'))
select.select_by_value('شتابدهنده')
