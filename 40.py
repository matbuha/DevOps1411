from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome(executable_path="C:/Users/UserPc/Desktop/deveops/chromedriver_win32/chromedriver.exe")
# my_driver.get("https://github.com")
# sleep(3)
# my_driver.close()
my_driver.get("C:/Users/UserPc/Desktop/deveops/tip_calc/index.html")
# my_driver.back()
# my_driver.refresh()
billamt = my_driver.find_element_by_id("billamt")
billamt.send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element_by_id('peopleamt').send_keys("4")
my_driver.find_element_by_id("musicquality").send_keys(2)
my_driver.find_element_by_id("calculate").click()
expected = "3.75"
actual = my_driver.find_element_by_id("tip").text

assert expected == actual
