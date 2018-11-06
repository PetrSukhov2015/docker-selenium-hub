import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        #self.browser = webdriver.Chrome()
	print (sys.argv[0])
	caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    	self.browser = webdriver.Remote(
        	command_executor='http://'+sys.argv[1]+':4444/wd/hub',
        	desired_capabilities=caps
    	)






    def test_github_repo_search(self):
        browser = self.browser
        browser.get('https://google.com')
	search_box = browser.find_element_by_name('q')  # Find search input box.
	search_box.send_keys('selenium')               # Type in selenium.
	search_box.send_keys(Keys.RETURN)              # Press ENTER.
	time.sleep(10)

        

#search_box = browser.find_element_by_name('q')
        #search_box.send_keys(Keys.RETURN)
        #time.sleep(10)  # simulate long running test
        #self.assertIn('Search more than', browser.page_source)



    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()

