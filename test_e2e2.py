# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# from utilities.BaseClass import BaseClass
#
#
# class TestTwo(BaseClass):
#
#     def test_e2e2(self):
#
#         self.driver.find_element_by_css_selector("a[href*='shop']").click()
#
#         products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#
#         for product in products:
#             productName = product.find_element_by_xpath("div/h4/a").text
#             if productName == "Blackberry":
#                 # Add item into cart/Click Add btn
#                 product.find_element_by_xpath("div[2]/button").click()
#
#         self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
#         self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
#         self.driver.find_element_by_id("country").send_keys("ind")
#
#         wait = WebDriverWait(self.driver, 8)
#         wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
#
#         # select 'India' from dropdown
#         self.driver.find_element_by_link_text("India").click()
#
#         checkbox = self.driver.find_element_by_css_selector("#checkbox2")
#         self.driver.execute_script("arguments[0].click();", checkbox)
#         print(checkbox.is_selected())       # True
#         assert checkbox.is_selected()
#
#
#         # click on Submit btn
#         self.driver.find_element_by_css_selector("[type='submit']").click()
#
#         successText = self.driver.find_element_by_class_name("alert-success").text
#
#         assert "Success! Thank you!" in successText







