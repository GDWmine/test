from selenium import webdriver
import time 

# 1.打开浏览器：实例化浏览器获得浏览器句柄（把柄）
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

# 2.打开网址
driver.get("http://132.232.44.158:8080/ljindex/")
driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()
time.sleep(1)
search_window = driver.current_window_handle 

driver.find_element_by_xpath('//*[@id="username"]').send_keys("15888880013")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="phonenum"]').send_keys("15888880013")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]').send_keys("15888880013")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="confirpw"]').send_keys("15888880013")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="emailnum"]').send_keys("15888880013@126.com")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="userRegist"]').click()
time.sleep(1)
dig_alert = driver.switch_to.alert
time.sleep(1)
try:
    assert dig_alert.text == "注册成功，请到个人中心设置密保问题，如不填写，你可能无法找回密码！"
    print("注册成功！")
except:
    print(dig_alert.text)
dig_alert.accept()
driver.quit()

# url = 'http://132.232.44.158:8080/ljindex/html/login.html'
# try:
#     url = 'http://132.232.44.158:8080/ljindex/html/login.html'
#     assert driver.current_url == url
#     print("注册成功！")
# except:
#     print(dig_alert.text)
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

# 2.打开网址
driver.get("http://132.232.44.158:8080/ljmanage/login.html")

driver.find_element_by_xpath('//*[@id="username"]').send_keys("gdwmine")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456789")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="adminLogin"]').click()

time.sleep(1)
search_window = driver.current_window_handle 

driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[3]/a/span').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="yhlist"]/ul/li/a').click()
driver.find_element_by_id('nickname_search').send_keys("15888880013")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search"]').click()

driver.find_element_by_id('nickname_search').send_keys("15888880013")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search"]').click()

