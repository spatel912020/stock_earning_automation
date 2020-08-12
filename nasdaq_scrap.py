from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '/home/shreyank99/Desktop/stock_earring_automation/stock_earning_automation/Selenium_Webdrivers/chromedriver'
driver = webdriver.Chrome(executable_path=PATH)
driver.get('https://nasdaq.com')

# ADD ALL DESIRED STOCK TICKERS FOR WEB CRAWL
stock_ticker = ['DIS', 'WM', 'WMT', 'CGC', 'MSFT']
earning_list = {}

# if you are using firefox brower, uncomment this section and comment google chrome section to run crawl
#PATH = '/home/shreyank99/Desktop/stock_earring_automation/stock_earning_automation/Selenium_Webdrivers/geckodriver'
#driver = webdriver.Firefox(executable_path=PATH)
#driver.get('https://nasdaq.com')
driver.maximize_window()

search_box = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/header/nav/div[2]/input')
search_box.click()
search_box = driver.find_element_by_xpath('//*[@id="search-overlay-input"]')
search_box.send_keys(stock_ticker[0])
wait = WebDriverWait(driver, 10)
first_company = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/ul/li[1]/a')))
#first_company = driver.find_element_by_css_selector('li.search-overlay__result:nth-child(1) > a:nth-child(1)')
first_company.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(2)

eps = driver.find_element_by_css_selector('body > div.dialog-off-canvas-main-canvas > div > main > div.page__content > div:nth-child(6) > div > div.quote-detail__top-grid-data > div > div.summary-data__table-container.loaded > table > tbody:nth-child(3) > tr:nth-child(3) > td.summary-data__cell')
#eps = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[6]/div/div[1]/div/div[2]/table/tbody[2]/tr[3]')

earning_list.update({stock_ticker[0] : eps.get_attribute('innerHTML')})
driver.execute_script("window.scrollTo(0, -1000)")
time.sleep(2)

for stock in stock_ticker[1:]:
	search_box = driver.find_element_by_xpath('//*[@id="find-symbol-input"]')
	search_box.click()
	search_box.send_keys(stock)
	driver.implicitly_wait(3)
	first_company = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[2]/div/div/div/div[1]/form/div/div/div/a[1]')
	first_company.click()
	time.sleep(2)
	driver.execute_script("window.scrollTo(0, 1000)")
	time.sleep(2)
	eps = driver.find_element_by_css_selector('body > div.dialog-off-canvas-main-canvas > div > main > div.page__content > div:nth-child(6) > div > div.quote-detail__top-grid-data > div > div.summary-data__table-container.loaded > table > tbody:nth-child(3) > tr:nth-child(3) > td.summary-data__cell')
	#eps = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[6]/div/div[1]/div/div[2]/table/tbody[2]/tr[3]')
	earning_list.update({stock : eps.get_attribute('innerHTML')})
	driver.execute_script("window.scrollTo(0, -1000)")
	time.sleep(2)

print(earning_list)
#eps = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div[6]/div/div[1]/div/div[2]/table/tbody[2]/tr[3]/td[2]')

driver.close()
