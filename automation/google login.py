from selenium import webdriver 
from time import sleep
driver = webdriver.Chrome("C:/Users/dell/Downloads/chromedriver.exe") 
driver.get('https://google.com')
sign_in=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/a')
sign_in.click()
Email=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
Email.send_keys('bnaskarb@gmail.com')
Next=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
Next.click()
sleep(8)