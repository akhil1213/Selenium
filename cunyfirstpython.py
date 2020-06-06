import time
from selenium import webdriver



def finish_enrolling(driver):
    while True:
        time.sleep(6)
        #proceed to step 2 of 3 button
        driver.find_element_by_xpath('/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[12]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/span/a').click()
        # driver.find_element_by_link_text("Proceed To Step 2 of 3").click()
        time.sleep(3)
        driver.find_element_by_link_text("Finish Enrolling").click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[5]/td[3]/div/div/table/tbody/tr[2]/td[8]/a').click()



def switch_frame(driver):
    template = driver.find_element_by_id("ptifrmtemplate")
    frmcontent = template.find_element_by_id("ptifrmcontent")
    iframe = frmcontent.find_element_by_tag_name("iframe")
    driver.switch_to.frame(iframe)
    driver.find_element_by_name("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3").click()
    time.sleep(4)
    driver.find_element_by_id("SSR_DUMMY_RECV1$sels$1$$0").click()
    driver.find_element_by_link_text("Continue").click()
    finish_enrolling(driver)


def enroll(driver):
    switch_frame(driver)
def login(driver):
    driver.find_element_by_id("CUNYfirstUsernameH").send_keys('username')
    driver.find_element_by_id("CUNYfirstPassword").send_keys('p123')
    time.sleep(2.0)
    driver.find_element_by_tag_name("button").click()
    driver.find_element_by_link_text("Student Center").click()
    enroll(driver)

def invoke_browser():
    driver = webdriver.Chrome('/home/akhil/Downloads/chromedriver')
    driver.get('https://home.cunyfirst.cuny.edu/psp/cnyepprd/EMPLOYEE/EMPL/h/?tab=DEFAULT')
    login(driver)


def main():
    invoke_browser()
if __name__ == '__main__':
    main()
