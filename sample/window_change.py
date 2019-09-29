import  time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('www.baidu.com')

#获得百度搜素窗口句柄
search_windows = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

