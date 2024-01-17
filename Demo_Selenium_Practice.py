# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
#
# driver.maximize_window()
#
# ele = driver.find_element(By.ID,"myTextInput2")
#
# result = ele.get_attribute('value')
# print(f"value : {result}")
# print(f"Type :{ele.get_attribute('type')}")
# print(f"Name :{ele.get_attribute('name')}")
# print(f"ID :{ele.get_attribute('id')}")
#
# time.sleep(5)



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
#
# driver.maximize_window()
#
# firstfeild = driver.find_element(By.ID,"myTextInput")
# firstfeild.send_keys("Lets Get started")
# print("=========================================")
# print("first Feild;")
# print(f"Value : {firstfeild.get_attribute('value')}")
# print(f"Type : {firstfeild.get_attribute('type')}")
# print(f"Name : {firstfeild.get_attribute('name')}")
# print(f"ID : {firstfeild.get_attribute('id')}")
# print("=========================================")
#
# secondfeild = driver.find_element(By.ID,"myTextarea")
# secondfeild.send_keys("Hello Guys")
# print("Second Feild;")
# print(f"Value : {secondfeild.get_attribute('value')}")
# print(f"Type : {secondfeild.get_attribute('type')}")
# print(f"Name : {secondfeild.get_attribute('name')}")
# print(f"ID : {secondfeild.get_attribute('id')}")
# print("=========================================")
#
# thirdfield = driver.find_element(By.ID,"myTextInput2")
# thirdfield.send_keys("This is Automation")
# print("Third Feild;")
# print(f"Value : {thirdfield.get_attribute('value')}")
# print(f"Type : {thirdfield.get_attribute('type')}")
# print(f"Name : {thirdfield.get_attribute('name')}")
# print(f"ID : {thirdfield.get_attribute('id')}")
# print("=========================================")
#
# fourthfeild = driver.find_element(By.ID,"myButton")
# fourthfeild.click()
# print("Fourth Feild;")
# print(f"Value : {fourthfeild.get_attribute('value')}")
# print(f"Type : {fourthfeild.get_attribute('type')}")
# print(f"Name : {fourthfeild.get_attribute('name')}")
# print(f"ID : {fourthfeild.get_attribute('id')}")
# print("=========================================")
#
# fifthfeild = driver.find_element(By.ID,"svgRect")
# fifthfeild.click()
# print("Fifth Feild;")
# print(f"Value : {fifthfeild.get_attribute('value')}")
# print(f"Type : {fifthfeild.get_attribute('type')}")
# print(f"Name : {fifthfeild.get_attribute('name')}")
# print(f"ID : {fifthfeild.get_attribute('id')}")
# print("=========================================")
#
# slider = driver.find_element(By.ID,"mySlider")
# slider.click()
#
#
# time.sleep(7)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r"https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_81h0iy9zyp_b&adgrpid=58575554323&hvpone=&hvptwo=&hvadid=617724335962&hvpos=&hvnetw=g&hvrand=16708825843251253407&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007786&hvtargid=kwd-64910771&hydadcr=15413_2322997&gclid=EAIaIQobChMIvraRluCX_AIVhINLBR2J9gy-EAAYASAAEgLT2vD_BwE")

driver.maximize_window()

search = driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("Boat Headphones")

clickSearchButton = driver.find_element(By.ID,"nav-search-submit-button")
clickSearchButton.click()

clickProduct = driver.find_element(By.CLASS_NAME,"s-image")
clickProduct.click()




time.sleep(15)