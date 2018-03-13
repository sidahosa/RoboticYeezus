from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Install and locate EXE path
driver=webdriver.Firefox(executable_path=r'C:\Users\Mobile-Xana\node_modules\geckodriver\geckodriver.exe')
driver.get('http://www.yeezysupply.com')

#-------------TEST ONLY-----------------
driver.find_element_by_xpath("//a[@href='/collections/look-3']").click()
driver.find_element_by_xpath("//a[@href='/products/ankle-boot-110mm-heel-python-dark/?back=%2Fcollections%2Flook-3']").click()
#---------------------------------------

#Default for any Yeezy shoes
myselect = Select(driver.find_element_by_class_name("PI__select.PI__input.js-select.js-select-SIZE.js-select-SIZE-static"))
try:
	#If the size wasn't available goes to next size
	myselect.select_by_visible_text("36").is_enabled()
	#Changed to popular size later
	print("36")
except:
	myselect.select_by_visible_text("40")
	print("40")

#Goes to Check Out
driver.find_element_by_xpath("//input[@type='submit' and @value='PURCHASE']").click()

#Goes to Shipping Page
driver.find_element_by_class_name("K__button.CA__button-checkout").click()

#WAIT in wait room
delay = 500 # seconds

WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "checkout_email")))


#Fill out address
driver.find_element_by_id("checkout_email").send_keys("familyguy3160@gmail.com")
driver.find_element_by_id("checkout_shipping_address_first_name").send_keys("Joe")
driver.find_element_by_id("checkout_shipping_address_last_name").send_keys("Johnson")
driver.find_element_by_id("checkout_shipping_address_address1").send_keys("1234 67th Ave")
driver.find_element_by_id("checkout_shipping_address_city").send_keys("Silver Spring")
driver.find_element_by_id("checkout_shipping_address_zip").send_keys("20901")
driver.find_element_by_id("checkout_shipping_address_phone").send_keys("3015558888")

driver.find_element_by_name("button").click()
driver.find_element_by_name("button").click()

#Credit Card Info
driver.find_element_by_id("checkout_different_billing_address_false").click()

driver.switch_to.frame(driver.find_element_by_xpath('//*[@title="Field container for: CARD NUMBER"]'))
cc = WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.NAME, "number")))
cc.clear()
cc.send_keys("1111")
cc.send_keys("2222")
cc.send_keys("3333")
cc.send_keys("4444")

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element_by_xpath("//*[@title='Field container for: NAME ON CARD']"))
dd = WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.NAME, "name")))
dd.send_keys("Joe B Johnson")

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element_by_xpath("//*[@title='Field container for: MM / YY']"))
rr = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "expiry")))
rr.send_keys("12")
rr.send_keys("20")

driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element_by_xpath("//*[@title='Field container for: CVV']"))
bb = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "verification_value")))
bb.send_keys("991")

driver.switch_to.default_content()

#Complete Order (This has been commented out to prevent the bot to actually ordering the shoes)
#driver.find_element_by_name("button").click()
print("You just copped (insert shoe here) via Selenium bot!")