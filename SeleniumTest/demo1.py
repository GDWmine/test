from selenium import webdriver
import time 

# 1.打开浏览器：实例化浏览器获得浏览器句柄（把柄）
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

# 2.打开网址
driver.get("http://132.232.44.158:8080/ljmanage/login.html")



driver.find_element_by_xpath('//*[@id="username"]').send_keys("gdwmine")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456789")
driver.find_element_by_xpath('//*[@id="adminLogin"]').click()


time.sleep(1)
search_window = driver.current_window_handle 

driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[3]/a/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="yhlist"]/ul/li/a').click()
driver.find_element_by_id('nickname_search').send_keys("浪晋超级帅")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search"]').click()

driver.find_element_by_id('nickname_search').send_keys("浪晋超级帅")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search"]').click()



