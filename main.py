from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options = chrome_options)

driver.get("https://www.portaljob-madagascar.com/")

try:
    search_box = driver.find_element(By.ID, "search_keywords")
    search_box.clear()
    search_box.send_keys("Odoo")
    search_box.send_keys(Keys.ENTER)
except Exception as e:
    assert False
