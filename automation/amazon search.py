##basically search on google open amzon/flipkart to watch out deals
from selenium import webdriver 
from time import sleep

class Amazon_Search:
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/dell/Downloads/chromedriver.exe")
        #self.username=username
        #self.password=password

    def searching_URL(self):
        driver=self.driver
        driver.get('https://www.amazon.com')

    def search_element(self):
        driver=self.driver
        sleep(3)
        search_box=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        search_box.send_keys("shoes")
        sleep(1)
        search_buttton_click=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
        search_buttton_click.click()

search=Amazon_Search()
search. searching_URL()
search.search_element()
