from selenium import webdriver
import time 

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

driver.get("http://master.aiguanxiao.com")

driver.find_element_by_xpath('//*[@id="username"]').send_keys("客服2.0g1")
driver.find_element_by_xpath('//*[@id="password_ipt"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="loginbtn"]').click()

time.sleep(1)
search_window = driver.current_window_handle 

driver.find_element_by_xpath('/html/body/div[2]/header/nav/div/ul[1]/li[3]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main-content"]/aside/section/ul/li[2]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main-content"]/aside/section/ul/li[2]/ul/li[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/table/tbody/tr[1]/td[18]/a[3]').click()
time.sleep(1)

driver.switch_to.frame("layui-layer-iframe1") 
driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[2]/div/div[1]/a').click()
time.sleep(1)

# driver.switch_to.frame("layui-layer-content") 
# driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[2]/div[1]/table/tbody/tr[2]/td[12]/div/a[1]').click()
# time.sleep(1)


