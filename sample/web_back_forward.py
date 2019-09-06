from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
first_url = 'http://www.baidu.com'
print('now access %s'%(first_url))

driver.get(first_url)

#进入新页面
second_url = 'https://www.zhihu.com.'
print('now access %s'%(first_url))
time.sleep(2)
driver.get(second_url)

#后退
print('back to  %s'%(second_url))
time.sleep(2)
driver.back()

#前进
print('forward to  %s'%(first_url))
driver.forward()

driver.quit()


