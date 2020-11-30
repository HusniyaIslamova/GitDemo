#101 We're trying to set this test/file44 with Page Object Mechanism. /Parametrizing Web-driver tests with Multiple Data sets

# File 44
#
#         driver = webdriver.Chrome()
#         driver.get("https://rahulshettyacademy.com/angularpractice")
#         driver.maximize_window()
#         driver.find_element_by_css_selector("input[name='name']").send_keys("Husniya")
#         driver.find_element_by_name("email").send_keys("Islamova")
#         driver.find_element_by_id("exampleCheck1").click()
#         sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#         sel.select_by_visible_text("Female")
#
#         driver.find_element_by_xpath("//input[@type='submit']").click()
#
#         message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
#         assert "Success" in message
# File 44 ends here

# #1. Lecture 101
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# class TestHomePage(BaseClass):
#
#     def test_fromSubmission(self, getData):
#
#         homepage = HomePage(self.driver)
#         homepage.getName().send_keys(getData[0])                                                                         #driver.find_element_by_css_selector("input[name='name']").send_keys("Husniya")
#         homepage.getEmail().send_keys(getData[1])                                                                       #driver.find_element_by_name("email").send_keys("Islamova")
#         homepage.getCheckBox().click()                                                                                  #driver.find_element_by_id("exampleCheck1").click()
#         self.selectOptionByText(homepage.getGender(), getData[2])                #a sel = Select(homepage.getGender())    #sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#         # Line above is inherited from BaseClass   # this a,b lines sent to BaseClass --> #b sel.select_by_visible_text("Female")
#
#         homepage.submitForm().click()                                                                                   #driver.find_element_by_xpath("//input[@type='submit']").click()
#
#         message = homepage.getSuccessMessage().text                                                                     #message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
#         assert "Success" in message
#         self.driver.refresh()
# # 1st run we send data for name, email, gender inputs, 2 run we try to send different data, we want system to delete data from 1st run, hence we use refresh() method,
#   #or we can make our test case independent from BaseClass and write get browser & url code in the beginning of the class (Lecture101 [9:00])
#
# # We won't add following fixture to conftest, because it's not common to all test cases
#     @pytest.fixture(params=[("Husniya","Islamova","Female"), ("Muhammadali", "Islamov", "Male")])
#     def getData(self, request):
#         return request.param


#2. Lecture 102. Modifying lecture 101, so we don't use index in lines a, b, c. In order to do that we modifying fixture, instead of tuple we use dictionary
# class TestHomePage(BaseClass):

    # def test_formSubmission(self, getData):
    #     log = self.getLogger()
    #     homepage = HomePage(self.driver)
    #     log.info("First name is " + getData["firstname"])   # or log.info("First name is " + getData["firstname"] + getData["lastname"])
    #     homepage.getName().send_keys(getData["firstname"])                #a
    #     homepage.getEmail().send_keys(getData["lastname"])               #b
    #     homepage.getCheckBox().click()
    #     self.selectOptionByText(homepage.getGender(), getData["gender"])  #c
    #
    #     homepage.submitForm().click()
    #
    #     message = homepage.getSuccessMessage().text
    #     assert "Success" in message
    #     self.driver.refresh()

    # @pytest.fixture(params=HomePageData.test_HomePage_data)      #syntax for calling class variable: className.variableName
    # def getData(self, request):
    #     return request.param

# Lecture 114. Getting data from Excel File for < def test_formSubmission  above

class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        message = homepage.getSuccessMessage().text
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param






