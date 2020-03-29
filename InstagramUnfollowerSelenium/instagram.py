from selenium import webdriver
from time import sleep
class InstaBot:
    def __init__(self):
        unfollowers = self.list_of_unfollowers()
        print(unfollowers)
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys("blank")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys("blank") 
        sleep(0.8)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        #logged in at this point
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'younginwabeard')]").click()
        sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[3]/a/span").click()
        self.open_followers()
        sleep(1)

        elements = self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
        # /html/body/div[3]/div/div[2]/ul/div/li/div/div[2]/div/div/div/a
        #get following button

        div_parent_of_button = elements[0].find_element_by_xpath(".//div/div[3]")
        button = div_parent_of_button.find_element_by_xpath(".//button")
        print(div_parent_of_button.get_attribute("class"))
        # button = button.find_element_by_xpath(".//button")

        for i in range(len(elements)):
            div_parent_of_a_tag = elements[i].find_element_by_xpath(".//div/div[2]/div")
            current_username = div_parent_of_a_tag.find_element_by_xpath(".//a")
            current_username = current_username.get_attribute("title")
            if current_username in unfollowers:
                button = elements[i].find_element_by_xpath(".//div/div[3]")
                button = button.find_element_by_xpath(".//button")
                button.click()
                unfollow_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]")
                unfollow_button.click()
                print(current_username)
            # print(current_username.get_attribute("title"))
        # /html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[2]/div/div/div/a
        # scroll_to_last_element_to_refresh = elements[len(elements)-1]
        # for element in elements:
        #     print(element.find_element_by_xpath("/div/div[1]/div[2]/div[1]/a"))
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # self.driver.excute_script('arguments[0].scrollIntoView()', sugs)
        sleep(1)
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        # last_ht, ht = 0,1
        # while last_ht != ht:
        #     last_ht = ht
        #     sleep(1)
        #     ht = self.driver.excute_script("""
        #     arguments[0].scrollTo(0,arguments[0].scrollHeight);
        #     return arguments[0].scrollHeight;
        #     """, scroll_box)
    def open_followers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
    def list_of_unfollowers(self):
        unfollowers_file = 'unfollowers.txt'
        unfollowers=[]
        with open(unfollowers_file) as fp:
            line = fp.readline()
            cnt  = 0
            while line:
                line = line[0:len(line)-1]#takes off \n
                if cnt%2==0:
                    unfollowers.append(line)
                line = fp.readline()
                cnt+=1
        return unfollowers
myBot = InstaBot()