from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import timeout_decorator
import sys
import time


url = "http://neutral.x0.com/home/sushida/play2.html"
driver = webdriver.Chrome("YOUR　SELENIUM　PATH")
driver.get(url)

k = input("連打をスタートするにはENTERを押してください")
print('終了するにはctrl+c')

clickaction =ActionChains(driver)
actions = ActionChains(driver)
clickaction.click()

@timeout_decorator.timeout(130)
def mainloop():
    while True:
        actions.send_keys("abcdefghijklmnopqrstuvwxyz-,").perform()


try:
    mainloop()
except:
    print('終了です')
else:
    print('終了できませんでした')
finally:
    driver.close()
