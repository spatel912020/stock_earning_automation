from selenium import webdriver

# 	web crawling for Chrome browser -- Uncomment if needed
#PATH = '/home/shreyank99/Desktop/stock_earring_automation/stock_earning_automation/Selenium_Webdrivers/chromedriver'
#driver = webdriver.Chrome(executable_path=PATH)
#driver.get('https://nasdaq.com')


PATH = '/home/shreyank99/Desktop/stock_earring_automation/stock_earning_automation/Selenium_Webdrivers/geckodriver'
driver = webdriver.Firefox(executable_path=PATH)
driver.get('https://nasdaq.com')
