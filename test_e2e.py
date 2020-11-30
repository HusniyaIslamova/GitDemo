import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()        # calling getLogger() method of BaseClass then assigning it to log variable
        homePage = HomePage(self.driver)       #a this line is written because HomePage class of HomePage file as a connection
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()        # we change this line to b line because of a line
        checkOutPage = homePage.shopItems()
        #cards = self.driver.find_elements_by_css_selector(".card-title a")
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)  #print(cardText)
            if cardText == "Blackberry":
                #self.driver.find_elements_by_css_selector(".card-footer button")[i].click()        # Add buttons
                checkOutPage.getCardFooter()[i].click()

        #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()                 # 1st 'Checkout' button
        checkOutPage.getCheckOut().click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()            # 2nd 'Checkout' button
        confirmPage = checkOutPage.CheckOutItems()

        #confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name as ind")
        #self.driver.find_element_by_id("country").send_keys("ind")
        confirmPage.getCountryInput().send_keys("ind")
        # time.sleep(5)
        #element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))        #a We moved this line to 'BaseClass' & instead we added b line
        self.verifyLinkPresence("India")                                                                                #b

        #self.driver.find_element_by_link_text("India").click()
        confirmPage.getIndiaOption().click()

        #self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmPage.getCheckBox().click()

        #self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmPage.getSubmit().click()

        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is" + textMatch)

        assert ("Success! Thank you!" in textMatch)
