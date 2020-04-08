from selenium import webdriver
from time import sleep

class TinderScraper():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/akhilkhanna/Downloads/chromedriver')
        self.driver.get("https://tinder.com")
        self.driver.maximize_window()
        sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button").click()
        sleep(6)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/button").click()
        # /html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[4]/div[1]/button
        
        #find the phone number button, it's always listed in a random order, first can be log in with google, then log in with phone number, etc
        elements = self.driver.find_elements_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/span/div")

        print(elements[0].find_element_by_xpath(".//button").get_attribute("aria-label"))
        sleep(5)
        phoneNumberElement = None
        for element in elements:
            print(element.find_element_by_xpath(".//button").get_attribute("aria-label"))
            if element.find_element_by_xpath(".//button").get_attribute("aria-label") == 'Log in with phone number':
                phoneNumberElement = element
        phoneNumberElement.click()
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button").click()
        sleep(2)
        #enter the phone number
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div/input").send_keys("9174153421")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button").click()
        #give the code received from my phone to the script using input
        print('Enter the code given to you from tinder:')
        code_from_tinder = input()


        #put the code in received from phone number.
        
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[1]").send_keys(code_from_tinder[0])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[2]").send_keys(code_from_tinder[1])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[3]").send_keys(code_from_tinder[2])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[4]").send_keys(code_from_tinder[3])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[5]").send_keys(code_from_tinder[4])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[3]/input[6]").send_keys(code_from_tinder[5])
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/button").click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
        sleep(3)
        self.clickButton("/html/body/div[2]/div/div/div/div/div[3]/button[1]")
        self.clickButton("/html/body/div[1]/div/div[3]/div/button")
        sleep(3)
        # self.clickButton("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[2]/div/div").click()
        # sleep(5)
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[3]/button[2]").click()
        scraped_bios = open("scraped_bios.txt", "w")
        while True:
            name = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span").getText()
            print(name)
            bio = self.readBio("/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[2]/div/span")
            print(bio)
            scraped_bios.write(name + "\'s bio is: " + bio + "\n")
            sleep(2)
        #like her and move on to the next
            self.clickButton("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button")
    def clickButton(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()
    def readBio(self,xpath):
        bioElements = self.driver.find_elements_by_xpath(xpath)
        currentBio = ""
        for element in bioElements:
            if element.get_attribute("class") == None:
                currentBio+= element.getText()
        return currentBio
myBot = TinderScraper()