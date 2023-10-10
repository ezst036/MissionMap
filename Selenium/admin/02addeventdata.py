from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

url = "http://ezst036.pythonanywhere.com/"
driver.get(url)

time.sleep(3)

'''
Admin user log in and add the permissions.
'''

loginlink = driver.find_element(By.LINK_TEXT, "Login")
loginhover = ActionChains(driver).move_to_element(loginlink)
loginhover.perform()
time.sleep(2)

loginlink.click()

time.sleep(2)

login = ActionChains(driver)
login.send_keys("fakeadmin01@fakeadmin01.com", Keys.TAB)
login.send_keys("removed", Keys.TAB)
login.send_keys(Keys.ENTER)
login.perform()

time.sleep(2)

hellolink = driver.find_element(By.LINK_TEXT, "Hello fakeadmin!")
hellohover = ActionChains(driver).move_to_element(hellolink)
hellohover.perform()
time.sleep(2)

hellolink.click()

adminlink = driver.find_element(By.LINK_TEXT, "Administration")
adminhover = ActionChains(driver).move_to_element(adminlink)
adminhover.perform()
time.sleep(2)

adminlink.click()

eventslink = driver.find_element(By.LINK_TEXT, "Events")
eventshover = ActionChains(driver).move_to_element(eventslink)
eventshover.perform()
time.sleep(2)

eventslink.click()

##########Add the first event
addeventslink = driver.find_element(By.LINK_TEXT, "ADD EVENT")
addeventshover = ActionChains(driver).move_to_element(addeventslink)
addeventshover.perform()
time.sleep(2)

addeventslink.click()

eventupdname = driver.find_element(By.ID, "id_name")
eventupdname.send_keys("First Event")

eventupddesc = driver.find_element(By.ID, "id_description")
eventupddesc.send_keys("First description")

eventupdprice = driver.find_element(By.ID, "id_price")
eventupdprice.send_keys("901", Keys.DELETE)

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()

time.sleep(3)

savelink.click()

##########Add the second event
addeventslink = driver.find_element(By.LINK_TEXT, "ADD EVENT")
addeventshover = ActionChains(driver).move_to_element(addeventslink)
addeventshover.perform()
time.sleep(2)

addeventslink.click()

eventupdname = driver.find_element(By.ID, "id_name")
eventupdname.send_keys("Second Event")

eventupddesc = driver.find_element(By.ID, "id_description")
eventupddesc.send_keys("Second description")

eventupdprice = driver.find_element(By.ID, "id_price")
eventupdprice.send_keys("908", Keys.DELETE)

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()

time.sleep(3)

savelink.click()

##########Add the third event
addeventslink = driver.find_element(By.LINK_TEXT, "ADD EVENT")
addeventshover = ActionChains(driver).move_to_element(addeventslink)
addeventshover.perform()
time.sleep(2)

addeventslink.click()

eventupdname = driver.find_element(By.ID, "id_name")
eventupdname.send_keys("Third Event")

eventupddesc = driver.find_element(By.ID, "id_description")
eventupddesc.send_keys("Third description")

eventupdprice = driver.find_element(By.ID, "id_price")
eventupdprice.send_keys("1234", Keys.DELETE)

time.sleep(2)

savelink = driver.find_element(By.NAME, "_save")
savehover = ActionChains(driver).move_to_element(savelink)
savehover.perform()

time.sleep(2)

savelink.click()

logoutlink = driver.find_element(By.LINK_TEXT, "LOG OUT")
logouthover = ActionChains(driver).move_to_element(logoutlink)
logouthover.perform()
logoutlink.click()

time.sleep(2)

menulink = driver.find_element(By.LINK_TEXT, "Events")
login.move_to_element(menulink).perform()
menulink.click()

time.sleep(7)