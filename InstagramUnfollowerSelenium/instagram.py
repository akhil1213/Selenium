from selenium import webdriver
from time import sleep
from logincredentials import username,password
class InstaBot:
    def __init__(self):
        self.unfollowers = self.list_of_unfollowers()
        
        self.driver = webdriver.Chrome('/home/akhil/Downloads/chromedriver')
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(3)
        self.login()
        
        #logged in at this point
        sleep(4)
        #click Not now since its in my way and then click on a tag to go on my profile
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'" + username + "')]").click()
        sleep(4)
        
        # self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[3]/a/span").click()
        
        self.open_followers()
        sleep(3)
        #get all of the seen elements inside of followers
        elements = self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
        sleep(2)
        # button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button")
        # button.click()
        index = 0
        while True:
            self.loop_through_followers(elements,index)
            #now scroll down to the last follower seen so it reloads and shows more followers after looping through current followers
            scroll_to_last_element_to_refresh = elements[index+6]
            self.driver.execute_script('arguments[0].scrollIntoView()', scroll_to_last_element_to_refresh)
            #elements must be recomputed because the page has refreshed with more 'following' users since it has scrolled to the 7th user.
            sleep(3)
            elements = self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
            print(len(elements))
            index+=6#because your checking 
        sleep(2)
        # scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        # last_ht, ht = 0,1
        # while last_ht != ht:
        #     last_ht = ht
        #     sleep(1)
        #     ht = self.driver.excute_script("""
        #     arguments[0].scrollTo(0,arguments[0].scrollHeight);
        #     return arguments[0].scrollHeight;
        #     """, scroll_box)
    def login(self):
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password) 
        sleep(0.8)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
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
    def loop_through_followers(self,elements,i):
        end = i + 6
        while i < end:
            div_parent_of_a_tag = elements[i].find_element_by_xpath(".//div/div[2]/div")
            current_username = div_parent_of_a_tag.find_element_by_xpath(".//a")
            current_username = current_username.get_attribute("title")
            sleep(4)
            if current_username in self.unfollowers:
                sleep(3)
                correct_index = i+1
                button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[" + str(correct_index)+ "]/div/div[2]/button")
                print(button.get_attribute("class"))
                button.click()
                print(current_username + "doesnt follow you but can't find that button")
                sleep(5)
                unfollow_button = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]")
                unfollow_button.click()
                sleep(5)
            print(i)
            print(current_username + "follows you")
            i+=1
            if i >= len(elements):
                break
myBot = InstaBot()
