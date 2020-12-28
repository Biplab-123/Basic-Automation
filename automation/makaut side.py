from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome("C:/Users/dell/Downloads/chromedriver.exe") 
driver.get('https://makaut1.ucanapply.com/smartexam/public/')
student_portal=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[1]/a/div/div[2]/div')
student_portal.click()
Roll_number=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/form/div[1]/div/div/input')
#Roll_number.click()
Roll_number.send_keys('12000317103')
sleep(15)