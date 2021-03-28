#we import sleep class from time module
from time import sleep,strftime
#we import webdriver class from selenium
from selenium import webdriver
#we import keys from selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys
#we import the randint from random
from random import randint
#we import pandas as pd its used to explore data sets
import pandas as pd
#from the webdriver class we call the firefox function and whatever is 
# is returned is stored in a 
# variable called browser
from selenium.webdriver.common.action_chains import ActionChains
#date
from datetime import datetime
from datetime import date    

browser = webdriver.Firefox()
#the browser waits for 5 seconds
browser.implicitly_wait(3)

#to open the url stated 
browser.get('https://kobo.humanitarianresponse.info/')

#after we sleep for 2 seconds
sleep(2)

username_input = browser.find_element_by_css_selector('#id_username')

password_input = browser.find_element_by_css_selector("#id_password")

#we send our credentials to those inputs
username_input.send_keys("tukwataniseray")

password_input.send_keys("Tukwatanise1")

sleep(randint(1,2))
#we look for the login button again
login_button = browser.find_element_by_xpath("/html/body/div/form/input[2]")
#and then we click it
login_button.click()
#we wait for 5 minutes
sleep(2)

#get the url
new_url = browser.current_url
print(new_url)
browser.get(new_url)

#First refresh the page
browser.refresh()
#relax
sleep(10)


#Now select he HVAT 
# select_hvat = browser.find_element_by_css_selector("li.asset-row:nth-child(3) > div:nth-child(1) > a:nth-child(1)")
select_hvat = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/ul/li[2]/div[1]")
# select_hvat = browser.find_elements_by_xpath("//*[contains(text(), 'ICYD Household Vulnerability Assessment Tool (HVAT) [OVCMIS FORM 007A')]").click()
select_hvat.click()

# browser.find_element_by_link_text("ICYD Household Vulnerability Assessment Tool (HVAT) [OVCMIS FORM 007A]").click()
sleep(1)
#we now get the current page
# new_url = browser.window_handles[0]
# print(new_url)
# #now open it 
# browser.switch_to.window(new_url)
form_url = browser.current_url
print(new_url)
browser.get(form_url)

# select_form = browser.find_element_by_class_name("form-view__tab")
select_form = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/a[2]")
select_form.click()
sleep(2)

#then select the open button

click_open_button = browser.find_element_by_css_selector(".collect-link")
click_open_button.click()
sleep(2)

#now must selenium to the nxt window tab
fill_in_form_url = browser.window_handles[1]
browser.switch_to.window(fill_in_form_url)

#get the url
fill_in_url = browser.current_url
print(fill_in_url)
browser.get(fill_in_url)

sleep(10)
#First refresh the page
browser.refresh()
#after getting the url then , i can now input the date

date_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[1]/div/input')
# date_input = browser.find_element_by_class_name('widgetdate')
our_date_today = date.today().isoformat()

date_input.send_keys(our_date_today)

#Type of Household which is New

sleep(1)

new_household = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[1]/fieldset/div/label[2]/input')
new_household.click()

sleep(2)
#scroll a little down
#select Accord

select_accord = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[3]/fieldset/div/label[2]/span')
select_accord.location_once_scrolled_into_view
# actions = ActionChains(browser)
# actions.move_to_element(select_accord).perform()
#Then click it 
select_accord.click()

#now click on the district picker
sleep(2)
district_picker = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[2]/div/button/span[1]')
district_picker.click()

#now select the kyenjojo
sleep(2)
select_kyenjojo = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[2]/div/ul/li[3]/a/label/span')
select_kyenjojo.click()

#now select kyenjogo town council
sleep(2)
select_kyenjojo_town_council = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[4]/fieldset/div/label[9]/span')
select_kyenjojo_town_council.click()

#I have skipped some things but ,i will come to them later
#Now let me input the community development Officer
sleep(2)
select_cdo = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/section/label[2]/input')
#input the name of cdo
cdo = 'KABAITIRA NAUME'
select_cdo.send_keys(cdo)

sleep(2)
#input the cdo telephone's number
# section.or-group-data:nth-child(5) > label:nth-child(2) > input:nth-child(3)
# /html/body/div[1]/article/form/section[2]/section[3]/section/label[3]/input
cdo_phone_number = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/section/label[3]/input')
# cdo_phone_number = browser.find_element_by_css_selector('section.or-group-data:nth-child(5) > label:nth-child(2) > input:nth-child(3)')
cdo_phone_number.location_once_scrolled_into_view
cdo_tele = 783323854
#input the number
cdo_phone_number.send_keys(cdo_tele)


