import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GithubSearchTest(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Chrome()
	caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    	self.browser = webdriver.Remote(
        	command_executor='http://localhost:4444/wd/hub',
        	desired_capabilities=caps
    	)



    def google_search(self):
	browser = self.browser
	browser.get("https://google.com/")
	search_box = driver.find_element_by_name('q')  # Find search input box.
	search_box.send_keys('selenium')               # Type in selenium.
	search_box.send_keys(Keys.RETURN)              # Press ENTER.
	#self.assertIn('selenium', browser.page_source)



    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()

