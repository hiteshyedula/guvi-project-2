from distutils.spawn import spawn
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Orange:
    url = "https://opensource-demo.orangehrmlive.com/"
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    def login(self):
        username = "Admin"
        password = "admin123"
        self.driver.get(self.url)
        time.sleep(2)

################ Sign IN  #######################
        username_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        username_finder = self.driver.find_element(by=By.XPATH, value=username_xpath)
        username_finder.send_keys(username)

        password_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        password_finder = self.driver.find_element(by=By.XPATH, value=password_xpath)
        password_finder.send_keys(password)
        

        sign_in_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        sign_in_finder = self.driver.find_element(by=By.XPATH, value=sign_in_xpath)
        sign_in_finder.click()
        time.sleep(2)
############### PIM  ##############################

        pim_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
        pim_finder = self.driver.find_element(by=By.XPATH, value=pim_xpath)
        pim_finder.click()
        time.sleep(2)

############# adding_user ###########################
        add_user_xpath = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
        add_user_finder = self.driver.find_element(by=By.XPATH, value=add_user_xpath)
        add_user_finder.click()
        time.sleep(4)
        
        first_name_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        first_name_finder = self.driver.find_element(by=By.XPATH, value=first_name_xpath)
        first_name_finder.send_keys("tester11")
        
        middle_name_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
        middle_name_finder = self.driver.find_element(by=By.XPATH, value=middle_name_xpath)
        middle_name_finder.send_keys("mid")

        last_name_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        last_name_finder = self.driver.find_element(by=By.XPATH, value=last_name_xpath)
        last_name_finder.send_keys("las")

        scroll_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
        scroll_finder = self.driver.find_element(by=By.XPATH, value=scroll_xpath)
        scroll_finder.click()
        time.sleep(3)

        usr_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
        usr_finder = self.driver.find_element(by=By.XPATH, value=usr_xpath)
        usr_finder.send_keys("hiteshtest")
        time.sleep(5)

        psw_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
        psw_finder = self.driver.find_element(by=By.XPATH, value=psw_xpath)
        psw_finder.send_keys("Tester@1233")
        time.sleep(5)

        psw_conf_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        psw_conf_finder = self.driver.find_element(by=By.XPATH, value=psw_conf_xpath)
        psw_conf_finder.send_keys("Tester@1233")
        time.sleep(5)

        sign_on_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        sign_on_finder = self.driver.find_element(by=By.XPATH, value=sign_on_xpath)
        sign_on_finder.click()
        time.sleep(5)

######################### Admin ###################################

        click_admin_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
        click_admin_finder = self.driver.find_element(by=By.XPATH, value=click_admin_xpath)
        click_admin_finder.click()

        adm_usr_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
        adm_usr_finder = self.driver.find_element(by=By.XPATH, value=adm_usr_xpath)
        adm_usr_finder.send_keys("hiteshtest")


        srch_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        srch_finder = self.driver.find_element(by=By.XPATH, value=srch_xpath)
        srch_finder.click()
        time.sleep(10)
######################## Logout ####################################
        logout_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
        logout_finder = self.driver.find_element(by=By.XPATH, value=logout_xpath)
        logout_finder.click()
        time.sleep(2)

        out_xpath = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
        out_finder = self.driver.find_element(by=By.XPATH, value=out_xpath)
        out_finder.click()
        time.sleep(2)
######################### New user login ###########################
        new_username_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        new_username_finder = self.driver.find_element(by=By.XPATH, value=new_username_xpath)
        new_username_finder.send_keys("hitesh1")

        new_password_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        new_password_finder = self.driver.find_element(by=By.XPATH, value=new_password_xpath)
        new_password_finder.send_keys("Tester@1233")
        

        sign_in_xpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        sign_in_finder = self.driver.find_element(by=By.XPATH, value=sign_in_xpath)
        sign_in_finder.click()
        time.sleep(2)



        time.sleep(2)


s = Orange()

s.login()