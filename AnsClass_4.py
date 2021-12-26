# 1.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

my_driver = webdriver.Chrome(executable_path="C:/Users/UserPc/Desktop/deveops/chromedriver_win32/chromedriver.exe")
"""my_driver.get("http://www.walla.co.il")
my_driver.get(" http://www.ynet.co.il")
sleep(3)
my_driver.close()

# 2.
my_title = my_driver.title
my_driver.refresh()
if my_title == my_driver.title:
    print("yesssssss!")"""


# 3. yes they're the same

# 4.
my_driver.get("https://translate.google.com")
my_driver.find_element_by_xpath("//textarea[@aria-label='טקסט מקור']").send_keys("הצלחתי!")

"""# 5.
my_driver.get("https://www.youtube.com/")
my_driver.find_element_by_xpath("//input[@id='search']").send_keys("nora en pure")
my_driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()

# 6.
my_driver.get("https://translate.google.com")
a = my_driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
b = my_driver.find_element_by_class_name("er8xn")
c = my_driver.find_element_by_xpath("//textarea[@aria-label='טקסט מקור']")
print(a)

# 7.
my_driver.get("https://www.facebook.com")
my_driver.find_element_by_xpath("//input[@id='email']").send_keys("EMAIL")
my_driver.find_element_by_xpath("//input[@id='pass']").send_keys("PASSWORD")
my_driver.find_element_by_xpath('//*[@id="u_0_d_Q9"]').click()

# 8.
my_driver.get("chrome://settings/clearBrowserData")
my_driver.find_element_by_xpath('//*[@id="clearBrowsingDataConfirm"]').click()
print("all cookies stored in the browser")

# 9.
my_driver.get("https://github.com")
my_driver.find_element_by_xpath("//input[@placeholder='Search GitHub']").send_keys("Selenium")
my_driver.find_element_by_xpath("//input[@placeholder='Search GitHub']").submit()

# 10.
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path=my_driver, chrome_options=chrome_options)
url = 'https://wwww.test.com/'
browser.get(url)
"""