from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)
'''
print('设置浏览器尺寸，参数时先宽后高')
driver.set_window_size(480,800)
'''
#driver.find_element_by_name('wd').send_keys("Selenium")
# driver.find_element_by_id("kw").send_keys("Selenium")
#driver.find_element_by_xpath("//*[@id='kw']").send_keys('虫师')
#river.find_element_by_css_selector('.s_ipt').send_keys('虫师')
driver.find_element_by_css_selector('#kw').send_keys('seleniums')
time.sleep(10)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()

测试测试测试
测试测试测试第三次