from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome("C:/Users/dell/Downloads/chromedriver.exe") 
driver.get('https://www.youtube.com')
searchbox=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/input')
searchbox.send_keys('mortal')
searchbutton=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button')
searchbutton.click()
sleep(10)