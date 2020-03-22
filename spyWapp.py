from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from dateutil.parser import *
import numpy as np
import matplotlib.pyplot as plt


def menu():
	print("Welcome to spyWapp ")
	print("Main Menu:-")
	print("1. Spy Contact")
	print("2. Schedule Message")
	print("3. Spam contact")
	print("4. Exit application")
	

def load_driver():
	options = webdriver.ChromeOptions()
	options.add_argument("user-data-dir=C:/Users/Aaron Ninan/AppData/Local/Google/Chrome/User Data/Default")
	driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', chrome_options=options)
	return driver


def open_wapp(driver):
	driver.get("https://web.whatsapp.com")

def get_diff(target_time):
	now = datetime.now()
	return (target_time-now).total_seconds()

def open_contact(contact , driver):
	new_chat_path = "//span[contains(@data-icon,'chat')]"
	new_chat_button = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(new_chat_path))
	new_chat_button.click()


	search_path = "(//div[contains(@class,'_3u328 copyable-text selectable-text')])[1]"
	search_button = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(search_path))
	search_button.click()
	search_button.send_keys(contact)

	time.sleep(2)

	selected_contact_path = "(//div[contains(@class,'xD91K')])[1]"
	selected_contact_button = driver.find_element_by_xpath("(//div[contains(@class,'xD91K')])[1]")
	selected_contact_button.click()

	time.sleep(2)


def schedule_msg(contact , text , driver ,target_time):
	time.sleep(get_diff(target_time))
	send_msg(contact , text , driver)


def send_msg(contact , text , driver ):
	open_contact(contact ,driver)

	
	msg_path = "//div[contains(@data-tab,'1')]"
	msg_box = driver.find_element_by_xpath(msg_path)

	msg_box.send_keys(text + Keys.ENTER)

def check_status(driver):
	_status = driver.find_element_by_css_selector('#main > header')
	status = _status.text

	if status.find('online') != -1:
		return 1
	else:
		 return 0

def spy(contact ,driver ,terminate_time):
	open_contact(contact ,driver)
	time.sleep(5)
	x=[]
	y=[]
	
	
	while(terminate_time > datetime.now()):

		if(check_status(driver)):
			print(datetime.now() ,"online")
			x.append(datetime.now())
			y.append(1)
			
				
		else:
			print(datetime.now() ,"offline")
			x.append(datetime.now())
			y.append(0)
			
				
		
	return x,y




           
            
def main():
	menu()
	inp=int(input("Enter option no. :"))

	if(inp==4):
		exit()
	if(inp==2):
		contact =input("Enter name of contact : ")
		text = input("Enter message to be sent : ")
		time_string = input("Enter time to send msg(Enter 0 if you want to send now) : ")
		target_time = parse(time_string)
		driver = load_driver()
		open_wapp(driver)
		time.sleep(4)
		schedule_msg(contact ,text , driver, target_time)

	if(inp==1):
		contact =input("Enter name of contact : ")
		terminate_string = input("Enter time at which spy should terminate : ")
		terminate_time = parse(terminate_string)
		driver = load_driver()
		open_wapp(driver)
		time.sleep(4)
		x,y = spy(contact , driver, terminate_time)
		plt.plot(x,y)
		plt.show()
		
	if(inp==3):
		contact =input("Enter name of contact : ")
		text = input("Enter spam text : ")
		repeat = int(input("Enter number of repeats : "))
		time_string = input("Enter time to spam(Enter 0 if you want to send now) : ")
		target_time = parse(time_string)
		driver = load_driver()
		open_wapp(driver)
		time.sleep(4)
		time.sleep(get_diff(target_time))
		for i in range(repeat):
			send_msg(contact ,text , driver)
			time.sleep(2)
		
	  
	main()

if __name__ == "__main__":
    main()


