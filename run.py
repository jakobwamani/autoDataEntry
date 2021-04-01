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
import openpyxl
#date
from datetime import datetime
from datetime import date    
import xlrd
import os

browser = webdriver.Firefox()
#the browser waits for 5 seconds
browser.implicitly_wait(3)

#to open the url stated 
browser.get('https://kobo.humanitarianresponse.info/')

#after we sleep for 2 seconds
sleep(1)

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
sleep(1)

#get the url
new_url = browser.current_url
print(new_url)
browser.get(new_url)

#First refresh the page
browser.refresh()
#relax
sleep(10)

#get the data from the excel sheet
df = pd.read_excel('tabulardata.xls', index_col=0)

#Now select he HVAT 
# select_hvat = browser.find_element_by_css_selector("li.asset-row:nth-child(3) > div:nth-child(1) > a:nth-child(1)")
select_hvat = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/ul/li[1]/div[1]/a")
# select_hvat = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/ul/li[2]/div[1]")
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
sleep(1)

#then select the open button

click_open_button = browser.find_element_by_css_selector(".collect-link")
click_open_button.click()
sleep(1)

#now must selenium to the nxt window tab
fill_in_form_url = browser.window_handles[1]
browser.switch_to.window(fill_in_form_url)

#get the url
fill_in_url = browser.current_url
print(fill_in_url)
sleep(3)
browser.get(fill_in_url)

sleep(15)
#First refresh the page
browser.refresh()
#after getting the url then , i can now input the date
sleep(3)
# /html/body/div[1]/article/form/section[2]/label[1]/div/input
date_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[1]/div/input')
# date_input = browser.find_element_by_class_name('widgetdate')
our_date_today = date.today().isoformat()

date_input.send_keys(our_date_today)

#Type of Household which is New

sleep(1)

new_household = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[1]/fieldset/div/label[2]/input')
new_household.click()

sleep(1)
#scroll a little down
#select Accord

select_accord = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[3]/fieldset/div/label[2]/span')
select_accord.location_once_scrolled_into_view
# actions = ActionChains(browser)
# actions.move_to_element(select_accord).perform()
#Then click it 
select_accord.click()

#now click on the district picker
sleep(1)
district_picker = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[2]/div/button/span[1]')
district_picker.click()

#now select the kyenjojo
sleep(1)
select_kyenjojo = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[2]/div/ul/li[3]/a/label/span')
select_kyenjojo.click()

#now select kyenjogo town council
sleep(1)
select_kyenjojo_town_council = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[4]/fieldset/div/label[9]/span')
select_kyenjojo_town_council.click()
sleep(1)


#I have skipped some things but ,i will come to them later

#service provider

service_p = df['service_provider'].values[0]
service_p_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/label[2]/input')
service_p_input.send_keys(service_p)

sleep(1)

service_p_tele = df['service_provider_tel'].values[0]
service_p_tele_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/label[3]/input')
service_p_tele_input.send_keys(str(service_p_tele))

#click on ownership
service_p_tele_owner = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/fieldset/fieldset/div/label[1]')
service_p_tele_owner.click()

#Now fill in that para social shit too
assessor_title_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[9]/label[4]/input')
#move to view
assessor_title_input.location_once_scrolled_into_view
assessor_title = 'PARA-SOCIAL-WORKER'
assessor_title_input.send_keys(assessor_title)
#Now let me input the community development Officer
sleep(1)

select_cdo = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/section/label[2]/input')
#input the name of cdo
cdo = 'KABAITIRA NAUME'
select_cdo.send_keys(cdo)

sleep(1)
#input the cdo telephone's number
# section.or-group-data:nth-child(5) > label:nth-child(2) > input:nth-child(3)
# /html/body/div[1]/article/form/section[2]/section[3]/section/label[3]/input
cdo_phone_number = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/section/label[3]/input')
# cdo_phone_number = browser.find_element_by_css_selector('section.or-group-data:nth-child(5) > label:nth-child(2) > input:nth-child(3)')
cdo_phone_number.location_once_scrolled_into_view
cdo_tele = 783323854
#input the number
cdo_phone_number.send_keys(cdo_tele)
sleep(1)

#select that the cdo own the phone number
self_owned_cdo_tele = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[3]/section/fieldset/fieldset/div/label[1]')
self_owned_cdo_tele.click()
sleep(1)

#i have skipped some things again
#this is now the supervisor part down below
supervisor_name = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[10]/label[2]/input')
#scroll_down
supervisor_name.location_once_scrolled_into_view
supervisor_full_names = 'KABAITIRA NAUME'
#input the name
supervisor_name.send_keys(supervisor_full_names)
sleep(1)

#supervisor tele
supervisor_tele = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[10]/label[3]/input')
#screw to view
supervisor_tele.location_once_scrolled_into_view
supervisor_tele_number = 783323854
supervisor_tele.send_keys(supervisor_tele_number)
sleep(1)

#include the supervisor title
supervisor_title_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[10]/label[4]/input')
#move to view
supervisor_title_input.location_once_scrolled_into_view
supervisor_title = 'SUPERVISOR'
supervisor_title_input.send_keys(supervisor_title)
sleep(1)

#include DPC name
dpc_name_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[11]/label[2]/input')
#move to view
dpc_name_input.location_once_scrolled_into_view
dpc_name = 'AGABA PHIONA'
dpc_name_input.send_keys(dpc_name)
sleep(1)

#include the DPC number 
dpc_number_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[11]/label[3]/input')
#move to view
dpc_number_input.location_once_scrolled_into_view
dpc_number = 782758476
dpc_number_input.send_keys(dpc_number)
sleep(1)

#give the title
dpc_title_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[11]/label[4]/input')
#move to view
dpc_title_input.location_once_scrolled_into_view
dpc_title = 'DPC'
dpc_title_input.send_keys(dpc_title)

#now select name of data entrant
select_data_entrant = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[11]/label[5]/div/button/span[1]')
sleep(1)
select_data_entrant.click()

#move to raymond
select_raymond = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[11]/label[5]/div/ul/li[11]/a/label/span')
#move to view
select_raymond.location_once_scrolled_into_view
#then click it
select_raymond.click()
sleep(1)


#come to 1.1 Who pays for most of the HH expenses?
#access the answer
print(df)
parishe = df['parish'].values[0]

#get to the parish
parish_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[3]/input')
#move to view
parish_input.location_once_scrolled_into_view
#input the parish
parish_input.send_keys(parishe)
sleep(1)

#village
village = df['village'].values[0]

village_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[4]/input')

village_input.location_once_scrolled_into_view

village_input.send_keys(village)
sleep(1)

#caregiver name
cg_name = df['caregiver'].values[0]

cg_name_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[2]/label[2]/input')

cg_name_input.location_once_scrolled_into_view

cg_name_input.send_keys(cg_name)
sleep(1)

#caregiver_tele
cg_tele = df['care_giver_tel'].values[0]

cg_tele_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[2]/label[3]/input')

cg_tele_input.location_once_scrolled_into_view

#remember to change the phone number into a string
cg_tele_input.send_keys(str(cg_tele))
sleep(1)

#caregiver_tele_ownership
cg_tele_custody = df['tel_ownership'].values[0]

#options
selfowned = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[2]/fieldset/fieldset/div/label[1]')
forother = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[2]/fieldset/fieldset/div/label[2]')
not_applicable = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/section[2]/fieldset/fieldset/div/label[3]')
sleep(1)
if(cg_tele_custody == 'SELF'):
    selfowned.location_once_scrolled_into_view
    selfowned.click()
elif(cg_tele_custody == 'FOROTHER'):
    forother.location_once_scrolled_into_view
    forother.click()
else:
    not_applicable.location_once_scrolled_into_view
    not_applicable.click()

sleep(1)
#include the serial number 
#grab the value from the excel sheet
serial_number = df['serial_number'].values[0]
serial_number_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[6]/input')
serial_number_input.location_once_scrolled_into_view
#dnot forget to change the df value to a string
serial_number_input.send_keys(str(serial_number))
sleep(1)

#age of household head
#grab the age from the excel sheet
age_of_cg = df['age_of_Cg'].values[0]
age_of_cg_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/label[9]/input')
age_of_cg_input.location_once_scrolled_into_view
#turn the age into a string
age_of_cg_input.send_keys(str(age_of_cg))

sleep(1)
#phase of administration
phase_time = df['phase'].values[0]
phase_time_in_str = str(phase_time)
#options
first_phase = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[5]/fieldset/div/label[1]')
second_phase = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[5]/fieldset/div/label[2]')
third_phase = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[5]/fieldset/div/label[3]')
fourth_phase = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[5]/fieldset/div/label[4]')
#make a decision
if(phase_time_in_str == '1'):
    first_phase.location_once_scrolled_into_view
    first_phase.click()
elif(phase_time_in_str == '2'):
    second_phase.location_once_scrolled_into_view
    second_phase.click()
elif(phase_time_in_str == '3'):
    third_phase.location_once_scrolled_into_view
    third_phase.click()
else:
    fourth_phase.location_once_scrolled_into_view
    fourth_phase.click()

sleep(1)

#sex of cg
#grab the value from the sheet
sex_of_cg = df['sex_of_cg'].values[0]
male_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[6]/fieldset/div/label[1]')
female_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[6]/fieldset/div/label[2]')

if(sex_of_cg == 'F'):
    female_cg.location_once_scrolled_into_view
    female_cg.click()
else:
    male_cg.location_once_scrolled_into_view
    male_cg.click()

sleep(1)

#Marital Status of HH Head/ primary Caregiver
marital_status = df['marital_status'].values[0]
marital_status_in_str = str(marital_status)
#options
single_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[7]/fieldset/div/label[1]')
married_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[7]/fieldset/div/label[2]')
widow_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[7]/fieldset/div/label[3]')
divorced_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[7]/fieldset/div/label[4]')
child_cg = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[7]/fieldset/div/label[5]')
#make a decision
if(marital_status_in_str == '1'):
    single_cg.location_once_scrolled_into_view
    single_cg.click()
elif(marital_status_in_str == '2'):
    married_cg.location_once_scrolled_into_view
    married_cg.click()
elif(marital_status_in_str == '3'):
    widow_cg.location_once_scrolled_into_view
    widow_cg.click()
elif(marital_status_in_str == '4'):
    divorced_cg.location_once_scrolled_into_view
    divorced_cg.click()
else:
    child_cg.location_once_scrolled_into_view
    child_cg.click()

sleep(1)   

#Education Level of HH Head/ Primary Caregiver
#pull the value from a spread_sheet
education_level = df['education'].values[0]
education_level_in_string = str(education_level)
#get the options
none_level = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[8]/fieldset/div/label[1]')
primary_level = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[8]/fieldset/div/label[2]')
secondary_level = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[8]/fieldset/div/label[3]')
tertiary_level = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[2]/fieldset[8]/fieldset/div/label[4]')
#make a decison
if(education_level_in_string == '1'):
    none_level.location_once_scrolled_into_view
    none_level.click()
elif(education_level_in_string == '2'):
    primary_level.location_once_scrolled_into_view
    primary_level.click()
elif(education_level_in_string == '3'):
    secondary_level.location_once_scrolled_into_view
    secondary_level.click()
else:
    tertiary_level.location_once_scrolled_into_view
    tertiary_level.click()
sleep(1)

#1.3 Are you a member of a savings group or association?
savings_group = df['one_point_three'].values[0]
#change it to string
savings_group_in_str = str(savings_group)
#make a binary dec
if(savings_group_in_str == '1'):
    savings_group_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[3]/fieldset/div/label[2]')
    savings_group_input.location_once_scrolled_into_view
    savings_group_input.click()
else:
    savings_group_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[3]/fieldset/div/label[1]')
    savings_group_input.location_once_scrolled_into_view
    savings_group_input.click()
sleep(1)

#1.4 How much have you saved in the last three months? (expressed in Uganda Shillings)
savings_in_three_months = df['one_point_four'].values[0]
#change to string
savings_in_three_months_in_str = str(savings_in_three_months)
#options
nothing = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[4]/fieldset/div/label[1]')
less_than_50k = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[4]/fieldset/div/label[2]')
fifty_k_to_one_fifty = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[4]/fieldset/div/label[3]')
one_fifty_to_three_hun = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[4]/fieldset/div/label[4]')
three_hun_and_above = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[4]/fieldset/div/label[5]')
#decision
if(savings_in_three_months_in_str == '4'):
    nothing.location_once_scrolled_into_view
    nothing.click()
elif(savings_in_three_months_in_str == '3'):
    less_than_50k.location_once_scrolled_into_view
    less_than_50k.click()
elif(fifty_k_to_one_fifty == '2'):
    fifty_k_to_one_fifty.location_once_scrolled_into_view
    fifty_k_to_one_fifty.click()
elif(one_fifty_to_three_hun == '1'):
    one_fifty_to_three_hun.location_once_scrolled_into_view
    one_fifty_to_three_hun.click()
else:
    three_hun_and_above.location_once_scrolled_into_view
    three_hun_and_above.click()
sleep(1)

#1.6 What is the current monthly HH income? (expressed in Uganda Shillings)* 
#pull value from execl
monthly_hh_income = df['one_point_six'].values[0]
#change to string
monthly_hh_income_in_str = str(monthly_hh_income)
#options
l_t_50k = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[6]/fieldset/div/label[1]')
fifty_to_ahun = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[6]/fieldset/div/label[2]')
ahun_to_one_fifty = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[6]/fieldset/div/label[3]')
one_fifty_to_two_hun = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[6]/fieldset/div/label[4]')
above_two_hun = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[6]/fieldset/div/label[5]')
#decision
if(monthly_hh_income_in_str == '4'):
    l_t_50k.location_once_scrolled_into_view
    l_t_50k.click()
elif(monthly_hh_income_in_str == '3'):
    fifty_to_ahun.location_once_scrolled_into_view
    fifty_to_ahun.click()
elif(monthly_hh_income_in_str == '2'):
    ahun_to_one_fifty.location_once_scrolled_into_view
    ahun_to_one_fifty.click()
elif(monthly_hh_income_in_str == '1'):
    one_fifty_to_two_hun.location_once_scrolled_into_view
    one_fifty_to_two_hun.click()
else:
    above_two_hun.location_once_scrolled_into_view
    above_two_hun.click()

sleep(1)

#1.7 What kinds of material goods or assets do you have?1) HH has an electronic gadget (Radio, Phone or TV)
#get value from sheet
gadget = df['one_point_seven_one'].values[0]
#to string
gadget_in_str = str(gadget)
#decision
if(gadget_in_str == '1'):
    gadget_true = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[1]/fieldset/div/label[1]')
    gadget_true.location_once_scrolled_into_view
    gadget_true.click()
else:
    gadget_false = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[1]/fieldset/div/label[2]')
    gadget_false.location_once_scrolled_into_view
    gadget_false.click()

sleep(1)

# 2) Any member of the HH has a functional means of transport (e.g. Bicycle, motorcycle, boat)
#value from sheet
transport_means = df['one_point_seven_two'].values[0]
#to_string
transport_means_in_str = str(transport_means)
#decision
if(transport_means_in_str == '1'):
    transport_available = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[2]/fieldset/div/label[1]')
    transport_available.location_once_scrolled_into_view
    transport_available.click()
else:
    transport_unavailable = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[2]/fieldset/div/label[2]')
    transport_unavailable.location_once_scrolled_into_view
    transport_unavailable.click()

sleep(1)

# 3) At least one member of the HH has vocational/apprenticeship/professional skills
vskills = df['one_point_seven_three'].values[0]
#to str
vskills_in_str = str(vskills)
#decision
if(vskills_in_str == '1'):
    vskills_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[3]/fieldset/div/label[1]')
    vskills_yes.location_once_scrolled_into_view
    vskills_yes.click() 
else:
    vskills_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[3]/fieldset/div/label[2]')
    vskills_no.location_once_scrolled_into_view
    vskills_no.click()

sleep(1)

# 4) At least one member of the HH has formal employment, is self-employed, or has a business
#excel
employment = df['one_point_seven_four'].values[0]
#str
employment_in_str = str(employment)
#decision
if(employment_in_str == '1'):
    has_employment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[4]/fieldset/div/label[1]')
    has_employment.location_once_scrolled_into_view
    has_employment.click()
else:
    no_employment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[4]/fieldset/div/label[2]')
    no_employment.location_once_scrolled_into_view
    no_employment.click()

sleep(1)

# 5) At least one member of the HH belongs to a savings group or association
belong_to_group = df['one_point_seven_five'].values[0]
#str
belong_to_group_in_str = str(belong_to_group)
#decision
if(belong_to_group_in_str == '1'):
    in_group = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[5]/fieldset/div/label[1]')
    in_group.location_once_scrolled_into_view
    in_group.click()
else:
    no_group = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[5]/fieldset/div/label[2]')
    no_group.location_once_scrolled_into_view
    no_group.click()

sleep(1)

# 6) HH has domestic animals (e.g. cow(s), goat(s), sheep, chicken(s), pig(s))

animals = df['one_point_seven_six'].values[0]
#str
animals_in_str = str(animals)
#decision
if(animals_in_str == '1'):
    has_animals = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[6]/fieldset/div/label[1]')
    has_animals.location_once_scrolled_into_view
    has_animals.click()
else:
    no_animals = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[6]/fieldset/div/label[2]')
    no_animals.location_once_scrolled_into_view
    no_animals.click()

sleep(1)

# 7) HH owns land
land = df['one_point_seven_seven'].values[0]
#str
land_in_str = str(land)
#decision
if(land_in_str == '1'):
    has_land = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[7]/fieldset/div/label[1]')
    has_land.location_once_scrolled_into_view
    has_land.click()
else:
    no_land = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[7]/fieldset/div/label[2]')
    no_land.location_once_scrolled_into_view
    no_land.click()

sleep(1)

# 8) HH has access to land for agriculture/hire
hire_land = df['one_point_seven_eight'].values[0]
#str
hire_land_in_str = str(hire_land)
#decision
if(hire_land_in_str == '1'):
    has_hire_land = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[8]/fieldset/div/label[1]')
    has_hire_land.location_once_scrolled_into_view
    has_hire_land.click()
else:
    no_hire_land = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[1]/fieldset[8]/fieldset/div/label[2]')
    no_hire_land.location_once_scrolled_into_view
    no_hire_land.click()

sleep(1)

# 1.8 If the HH incurred any of the following expenses in the past three months, was it able to pay without difficulty, e.g., without selling HH permanent assets like land or bicycle or without borrowing?
# 1) Health-related expenses (Yes/No/NA)

health_expenses = df['one_point_eight_one'].values[0]
#str
health_expenses_in_str = str(health_expenses)
#decision
if(health_expenses_in_str == '1'):
    sickly = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[1]/fieldset/div/label[1]')
    sickly.location_once_scrolled_into_view
    sickly.click()
else:
    healthy = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[1]/fieldset/div/label[2]')
    healthy.location_once_scrolled_into_view
    healthy.click()

sleep(1)

# 2) Education (school)-related expenses (Yes/No/NA)
education_expense = df['one_point_eight_two'].values[0]
#str
education_expense_in_str = str(education_expense)
#decision
if(education_expense_in_str == '1'):
    schooling = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[2]/fieldset/div/label[1]')
    schooling.location_once_scrolled_into_view
    schooling.click()
else:
    no_schooling = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[2]/fieldset/div/label[2]')
    no_schooling.location_once_scrolled_into_view
    no_schooling.click()

sleep(1)

# 3) Food-related expenses (Yes/No/NA)
food_expense = df['one_point_eight_three'].values[0]
#str
food_expense_in_str = str(food_expense)
#decision
if(food_expense_in_str == '1'):
    eating = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[3]/fieldset/div/label[1]')
    eating.location_once_scrolled_into_view
    eating.click()
else:
    hungry = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/section[2]/fieldset[3]/fieldset/div/label[2]')
    hungry.location_once_scrolled_into_view
    hungry.click()

sleep(1)
# PRIORITY AREA 2: SURVIVAL AND HEALTH
# 2.1 Over the past month [state the month], what has been the main source of food consumed by the members of your HH?
food_source = df['two_point_one'].values[0]
#str
food_source_in_str = str(food_source)
#options
donated = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[1]/fieldset/div/label[1]')
work_to_eat = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[1]/fieldset/div/label[2]')
market = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[1]/fieldset/div/label[3]')
home_grown_plus_wte = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[1]/fieldset/div/label[4]')
homegrown = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[1]/fieldset/div/label[5]')
#decision

if(food_source_in_str == '4'):
    donated.location_once_scrolled_into_view
    donated.click()
elif(food_source_in_str == '3'):
    work_to_eat.location_once_scrolled_into_view
    work_to_eat.click()
elif(food_source_in_str == '2'):
    market.location_once_scrolled_into_view
    market.click()
elif(home_grown_plus_wte == '1'):
    home_grown_plus_wte.location_once_scrolled_into_view
    home_grown_plus_wte.click()
else:
    homegrown.location_once_scrolled_into_view
    homegrown.click()

sleep(1)
# 2.2 What does the family usually eat (at least 3 times a week)?
# 1). Energy foods: potatoes, bananas, oils, posho, millet, rice, maize, bread, cassava
energy_food = df['two_point_two_one'].values[0]
#to str
energy_food_to_str = str(energy_food)
#decision
if(energy_food_to_str == '1'):
    energy_food_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[1]/fieldset/div/label[1]')
    energy_food_yes.location_once_scrolled_into_view
    energy_food_yes.click()
else:
    energy_food_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[1]/fieldset/div/label[2]')
    energy_food_no.location_once_scrolled_into_view
    energy_food_no.click()

sleep(1)

# 2). Body-building foods: beans, meat, soya, peas, milk, eggs, chicken, fish
building_food = df['two_point_two_two'].values[0]
#to ste
building_food_to_str = str(building_food)
#decision
if(building_food_to_str == '1'):
    building_food_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[2]/fieldset/div/label[1]')
    building_food_yes.location_once_scrolled_into_view
    building_food_yes.click()
else:
    building_food_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[2]/fieldset/div/label[2]')
    building_food_no.location_once_scrolled_into_view
    building_food_no.click()

sleep(1)

# 3). Protective and regulative foods: tomatoes, oranges, paw paw, mangoes, pineapples
regular_food = df['two_point_two_three'].values[0]
#to str
regular_food_in_str = str(regular_food)
#decision
if(regular_food_in_str == '1'):
    regular_food_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[3]/fieldset/div/label[1]')
    regular_food_yes.location_once_scrolled_into_view
    regular_food_yes.click()
else:
    regular_food_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[1]/fieldset[3]/fieldset/div/label[2]')
    regular_food_no.location_once_scrolled_into_view
    regular_food_no.click()

sleep(1)

# 2.3 How many meals does the HH have in a day?
meals = df['two_point_three'].values[0]
#to str
meals_in_str = str(meals)
#options
no_meal = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[2]/fieldset/div/label[1]')
one_meal = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[2]/fieldset/div/label[2]')
two_meal = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[2]/fieldset/div/label[3]')
three_meal = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[2]/fieldset/div/label[4]')
#decision
if(meals_in_str == '4'):
    no_meal.location_once_scrolled_into_view
    no_meal.click()
elif(meals_in_str == '3'):
    one_meal.location_once_scrolled_into_view
    one_meal.click()
elif(meals_in_str == '1'):
    two_meal.location_once_scrolled_into_view
    two_meal.click()
else:
    three_meal.location_once_scrolled_into_view
    three_meal.click()
    
sleep(1)
# 2.4 In the past month [state the month], has any member of the HH gone a whole day and night without eating anything at all due to lack of food?
lack_of_food = df['two_point_four'].values[0]
#str
lack_of_food_in_str = str(lack_of_food)
#decision
if(lack_of_food_in_str == '1'):
    lack_of_food_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[3]/fieldset/div/label[1]')
    lack_of_food_yes.location_once_scrolled_into_view
    lack_of_food_yes.click()
else:
    lack_of_food_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[3]/fieldset/div/label[2]')
    lack_of_food_no.location_once_scrolled_into_view
    lack_of_food_no.click()

sleep(1)

# 2.6 Do the following apply to this HH? [Observe for yourself where applicable]
# 1). HH harvests rain water or has access to safe water within 30 minutes (half an hour) for domestic use
rainwater = df['two_point_six_one'].values[0]
#str
rainwater_in_str = str(rainwater)
#decision
if(rainwater_in_str == '1'):
    rainwater_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[1]/fieldset/div/label[1]')
    rainwater_yes.location_once_scrolled_into_view
    rainwater_yes.click()
else:
    rainwater_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[1]/fieldset/div/label[2]')
    rainwater_no.location_once_scrolled_into_view
    rainwater_no.click()

sleep(1)

# 2). HH has access to a public health facility within 5 kilometers
health_access = df['two_point_six_two'].values[0]
health_access_in_str = str(health_access)
#Decision
if(health_access_in_str == '1'):
    health_access_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[2]/fieldset/div/label[1]')
    health_access_yes.location_once_scrolled_into_view
    health_access_yes.click()
else:
    health_access_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[2]/fieldset/div/label[2]')
    health_access_no.location_once_scrolled_into_view
    health_access_no.click()
sleep(1)
# 3).All HH members sleep under a mosquito net
net = df['two_point_six_three'].values[0]
net_in_str = str(net)
#decision
if(net_in_str == '1'):
    net_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[3]/fieldset/div/label[1]')
    net_yes.location_once_scrolled_into_view
    net_yes.click()
else:
    net_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[3]/fieldset/div/label[2]')
    net_no.location_once_scrolled_into_view
    net_no.click()
sleep(1)
# 4). HH has a latrine/toilet facility used by the members of the HH
toilet = df['two_point_six_four'].values[0]
toilet_in_str = str(toilet)
#decision
if(toilet_in_str == '1'):
    toilet_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[4]/fieldset/div/label[1]')
    toilet_yes.location_once_scrolled_into_view
    toilet_yes.click()
else:
    toilet_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[4]/fieldset/div/label[2]')
    toilet_no.location_once_scrolled_into_view
    toilet_no.click()

sleep(1)

# 5). HH has a handwashing facility
washing = df['two_point_six_five'].values[0]
washing_in_str = str(washing)
#decision
if(washing_in_str == '1'):
    washing_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[5]/fieldset/div/label[1]')
    washing_yes.location_once_scrolled_into_view
    washing_yes.click()
else:
    washing_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[5]/fieldset/div/label[2]')
    washing_no.location_once_scrolled_into_view
    washing_no.click()

sleep(1)

# 6). HH has a separate house for a kitchen
kitchen = df['two_point_six_six'].values[0]
kitchen_in_str = str(kitchen)
#decision
if(kitchen_in_str == '1'):
    kitchen_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[6]/fieldset/div/label[1]')
    kitchen_yes.location_once_scrolled_into_view
    kitchen_yes.click()
else:

    kitchen_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/section[2]/fieldset[6]/fieldset/div/label[2]')
    kitchen_no.location_once_scrolled_into_view
    kitchen_no.click()

sleep(1)

# 2.7 Does the HH have a person with a disability?
disability = df['two_point_seven'].values[0]
disability_in_str = str(disability)
#decision
if(disability_in_str == '1'):
    disability_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[5]/fieldset/div/label[1]')
    disability_yes.location_once_scrolled_into_view
    disability_yes.click()
else:
    disability_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[5]/fieldset/div/label[2]')
    disability_no.location_once_scrolled_into_view
    disability_no.click()

sleep(1)

# 2.8 Does any person in the HH have a long - term illness?
ill = df['two_point_eight'].values[0]
ill_in_str = str(ill)
#decision
if(ill_in_str == '1'):
    
    ill_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[6]/fieldset/div/label[1]')
    ill_yes.click()
else:
    ill_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[6]/fieldset/div/label[2]')
    ill_no.click()

sleep(1)

# 2.9 Have all children in need of health services for chronic illnesses and/or disability been referred for and are receiving the necessary treatment?
referral = df['two_point_nine'].values[0]
#str 
referral_in_str = str(referral)
#options
none_referral = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[7]/fieldset/div/label[1]')
less_than_fifty = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[7]/fieldset/div/label[2]')
fifty_or_more = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[7]/fieldset/div/label[3]')
all_chronically = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[7]/fieldset/div/label[4]')
#decision
if(referral_in_str == '4'):
    none_referral.location_once_scrolled_into_view
    none_referral.click()
elif(referral_in_str == '3'):
    less_than_fifty.location_once_scrolled_into_view
    less_than_fifty.click()
elif(referral_in_str == '2'):
    fifty_or_more.location_once_scrolled_into_view
    fifty_or_more.click()
else:
    all_chronically.location_once_scrolled_into_view
    all_chronically.click()

sleep(1)

# 2.10 Does the caregiver know the HIV status of all members in the HH in the last six months?
hivstatus = df['two_point_ten'].values[0]
#str
hivstatus_to_str = str(hivstatus)
#options
knows_none = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[8]/fieldset/div/label[1]')
knows_less_than_fifty = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[8]/fieldset/div/label[2]')
knows_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[8]/fieldset/div/label[3]')
knows_more_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[8]/fieldset/div/label[4]')
knows_all_status = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[8]/fieldset/div/label[5]')

#decision
if(hivstatus_to_str == '4'):
    knows_none.location_once_scrolled_into_view
    knows_none.click()
elif(hivstatus_to_str == '3'):
    knows_less_than_fifty.location_once_scrolled_into_view
    knows_less_than_fifty.click()
elif(hivstatus_to_str == '2'):
    knows_half.location_once_scrolled_into_view
    knows_half.click()
elif(hivstatus_to_str == '1'):
    knows_more_than_half.location_once_scrolled_into_view
    knows_more_than_half.click()
else:
    knows_all_status.location_once_scrolled_into_view
    knows_all_status.click()

sleep(1)

# 2.11 Are all eligible HH members who are HIV+ and/or have tuberculosis on care or treatment? Yes/No/NA (If Yes, request ART/Health card)
ontreatment = df['two_point_eleven'].values[0]
#str
ontreatment_in_str = str(ontreatment)
#options
none_on_treatment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[9]/fieldset/div/label[1]')
less_than_half_on_treatment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[9]/fieldset/div/label[2]')
half_on_treatment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[9]/fieldset/div/label[3]')
more_than_half_on_treatment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[9]/fieldset/div/label[4]')
all_on_treatment = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[9]/fieldset/div/label[5]')

#decision
if(ontreatment_in_str == '4'):
    none_on_treatment.location_once_scrolled_into_view
    none_on_treatment.click()
elif(ontreatment_in_str == '3'):
    less_than_half_on_treatment.location_once_scrolled_into_view
    less_than_half_on_treatment.click()
elif(ontreatment_in_str == '2'):
    half_on_treatment.location_once_scrolled_into_view
    half_on_treatment.click()
elif(ontreatment_in_str == '1' ):
    more_than_half_on_treatment.location_once_scrolled_into_view
    more_than_half_on_treatment.click()
else:
    all_on_treatment.location_once_scrolled_into_view
    all_on_treatment.click()

sleep(1)

# 2.12 Are all the HH members who are HIV+ adhering to treatment as prescribed?
adhering = df['two_point_twelve'].values[0]
adhering_in_str = str(adhering)
#options
none_adhering = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[10]/fieldset/div/label[1]')
less_than_half_adhering = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[10]/fieldset/div/label[2]')
half_adhering = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[10]/fieldset/div/label[3]')
more_than_half_adhering = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[10]/fieldset/div/label[4]')
all_adhering = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[10]/fieldset/div/label[5]')
#decision

if(adhering_in_str == '4'):
    none_adhering.location_once_scrolled_into_view
    none_adhering.click()

elif(adhering_in_str == '3'):
    less_than_half_adhering.location_once_scrolled_into_view
    less_than_half_adhering.click()
elif(adhering_in_str == '2'):
    half_adhering.location_once_scrolled_into_view
    half_adhering.click()
elif(adhering_in_str == '1'):
    more_than_half_adhering.location_once_scrolled_into_view
    more_than_half_adhering.click()
else:
    all_adhering.location_once_scrolled_into_view
    all_adhering.click()

sleep(1)

# 2.13 Have all the eligible HH members ever done a blood test called viral load (VL) in the last six (6) months?*
vltest = df['two_point_thirteen'].values[0]
#str
vltest_in_str = str(vltest)
# options
vltest_none = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[11]/fieldset/div/label[1]')
vltest_less_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[11]/fieldset/div/label[2]')
vltest_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[11]/fieldset/div/label[3]')
vltest_more_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[11]/fieldset/div/label[4]')
vltest_done = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[11]/fieldset/div/label[5]')
#decision
if(vltest_in_str == '4'):
    vltest_none.location_once_scrolled_into_view
    vltest_none.click()
elif(vltest_in_str == '3'):
    vltest_less_than_half.location_once_scrolled_into_view
    vltest_less_than_half.click()
elif(vltest_half == '2'):
    vltest_half.location_once_scrolled_into_view
    vltest_half.click()
elif(vltest_more_than_half == '1'):
    vltest_more_than_half.location_once_scrolled_into_view
    vltest_more_than_half.click()
else:
    vltest_done.location_once_scrolled_into_view
    vltest_done.click()

sleep(1)

# 2.14 Is the viral load for all the HH members who are HIV+ suppressed?
suppressed = df['two_point_fourteen'].values[0]
#str
suppressed_in_str = str(suppressed)

#options
suppressed_none = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[12]/fieldset/div/label[1]')
suppressed_less_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[12]/fieldset/div/label[2]')
suppressed_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[12]/fieldset/div/label[3]')
suppressed_more_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[12]/fieldset/div/label[4]')
suppressed_all = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[12]/fieldset/div/label[5]')
#decision
if(suppressed_in_str == '4'):
    suppressed_none.location_once_scrolled_into_view
    suppressed_none.click()
elif(suppressed_in_str == '3'):
    suppressed_less_than_half.location_once_scrolled_into_view
    suppressed_less_than_half.click()
elif(suppressed_in_str == '2'):
    suppressed_half.location_once_scrolled_into_view
    suppressed_half.click()
elif(suppressed_in_str == '1'):
    suppressed_more_than_half.location_once_scrolled_into_view
    suppressed_more_than_half.click()
else:
    suppressed_all.location_once_scrolled_into_view
    suppressed_all.click()

sleep(1)

# 2.15 Does the HH have a stable shelter that is adequate, safe, and dry?
shelter = df['two_point_fifteen'].values[0]
#str
shelter_in_str = str(shelter)
#options
no_shelter = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[13]/fieldset/div/label[1]')
shelter_major_repairs = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[13]/fieldset/div/label[2]')
shelter_some_repairs = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[13]/fieldset/div/label[3]')
shelter_fair = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[13]/fieldset/div/label[4]')
shelter_is_safe = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[5]/fieldset[13]/fieldset/div/label[5]')
if(shelter_in_str == '4'):
    no_shelter.location_once_scrolled_into_view
    no_shelter.click()
elif(shelter_in_str == '3'):
    shelter_major_repairs.location_once_scrolled_into_view
    shelter_major_repairs.click()
elif(shelter_in_str == '2'):
    shelter_some_repairs.location_once_scrolled_into_view
    shelter_some_repairs.click()
elif(shelter_in_str == '1'):
    shelter_fair.location_once_scrolled_into_view
    shelter_fair.click()
else:
    shelter_is_safe.location_once_scrolled_into_view
    shelter_is_safe.click()

sleep(1)

# 3.1 Are all children aged 6–17 years in this HH enrolled in school ,vocational training or apprenticeship?
school_enroll = df['three_point_one'].values[0]
#str
school_enroll_str = str(school_enroll)
#decision
if(school_enroll_str == '1'):
    school_enroll_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[1]/fieldset/div/label[2]')
    school_enroll_no.location_once_scrolled_into_view
    school_enroll_no.click()
else:
    school_enroll_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[1]/fieldset/div/label[1]')
    school_enroll_yes.location_once_scrolled_into_view
    school_enroll_yes.click()

sleep(1)
# 3.2 Have all the children aged 6-17 years in this HH attended school, vocational training or apprenticeship regularly (At least 4 days a week on average) in the past 12 months
school_attendance = df['three_point_two'].values[0]
#str
school_attendance_str = str(school_attendance)
#decision
if(school_attendance_str == '1'):
    absentee = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[2]/fieldset/div/label[1]')
    absentee.location_once_scrolled_into_view
    absentee.click()
else:
    attendee = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[2]/fieldset/div/label[2]')
    attendee.location_once_scrolled_into_view
    attendee.click()
sleep(1)

# 3.3 How many children aged 3-5 years in this HH are not enrolled in Pre-school or have have missed Preschool 3 or more times a week?
miss_school = df['three_point_three'].values[0]
#str
miss_school_str =str(miss_school)
#options
miss_school_three_more_times = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[3]/fieldset/div/label[1]')
miss_school_less_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[3]/fieldset/div/label[2]')
miss_school_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[3]/fieldset/div/label[3]')
miss_school_more_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[3]/fieldset/div/label[4]')
miss_school_none = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[6]/fieldset[3]/fieldset/div/label[5]')

#decision
if(miss_school_str == '4'):
    miss_school_three_more_times.location_once_scrolled_into_view
    miss_school_three_more_times.click()
elif(miss_school_str == '3'):
    miss_school_less_than_half.location_once_scrolled_into_view
    miss_school_less_than_half.click()
elif(miss_school_str == '2'):
    miss_school_half.location_once_scrolled_into_view
    miss_school_half.click()
elif(miss_school_str == '1'):
    miss_school_more_than_half.location_once_scrolled_into_view
    miss_school_more_than_half.click()
else:
    miss_school_none.location_once_scrolled_into_view
    miss_school_none.click()


sleep(1)

#4.1 In the past 12 months, have all the children in the HH been under the care of and lived with the same adult primary caregiver
care = df['four_point_one'].values[0]
#str
care_str = str(care)
#decision
if(care_str == '1'):
    no_care = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[1]/fieldset/div/label[2]')
    no_care.location_once_scrolled_into_view
    no_care.click()
else:
    yes_care = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[1]/fieldset/div/label[1]')
    yes_care.location_once_scrolled_into_view
    yes_care.click()

sleep(1)
# 4.2 In the past 6 months, are there any children in this HH who are withdrawn or consistently sad, unhappy, depressed and not able to participate in daily activities including playing with friends and family?
activity = df['four_point_two'].values[0]
#str
activity_str = str(activity)
#options
all_children = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[2]/fieldset/div/label[1]')
half_or_more = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[2]/fieldset/div/label[2]')
less_than_half = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[2]/fieldset/div/label[3]')
none_activity = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[2]/fieldset/div/label[4]')
#decision 
if(activity_str == '4'):
    all_children.location_once_scrolled_into_view
    all_children.click()
elif(activity_str == '3'):
    half_or_more.location_once_scrolled_into_view
    half_or_more.click()
elif(activity_str == '2'):
    less_than_half.location_once_scrolled_into_view
    less_than_half.click()
else:
    none_activity.location_once_scrolled_into_view
    none_activity.click()

sleep(1)

# 4.3 What would you do if any of your children experienced or became a victim of child abuse or violence?
abuse = df['four_point_three'].values[0]
#str
abuse_str = str(abuse)
#options
nothing = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[3]/fieldset/div/label[1]')
neighbour = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[3]/fieldset/div/label[2]')
report = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/fieldset[3]/fieldset/div/label[3]')

#decision
if(abuse_str == '4'):
    nothing.location_once_scrolled_into_view
    nothing.click()
elif(abuse_str == '1'):
    neighbour.location_once_scrolled_into_view
    neighbour.click()
else:
    report.location_once_scrolled_into_view
    report.click()

sleep(1)

# 4.4 In the past 6 months, has any child in the HH has the following happen to them in or outside the HH
# 1) The child experienced repeated physical abuse that caused body harm

harm = df['four_point_four_one'].values[0]
#str
harm_str = str(harm)
#decision
if(harm_str == '1'):
    harm_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[1]/fieldset/div/label[1]')
    harm_yes.location_once_scrolled_into_view
    harm_yes.click()
else:
    harm_no =browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[1]/fieldset/div/label[2]')
    harm_no.location_once_scrolled_into_view
    harm_no.click()

sleep(1)

# 2) A meal was withheld to punish the child. (Yes / No)

punish = df['four_four_two'].values[0]
#punish str
punish_str = str(punish)
#decsion
if(punish_str == '1'):
    punish_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[2]/fieldset/div/label[1]')
    punish_yes.location_once_scrolled_into_view
    punish_yes.click()
else:
    punish_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[2]/fieldset/div/label[2]')
    punish_no.location_once_scrolled_into_view
    punish_no.click()

sleep(1)

# 3) The child was involved in Child Labour.
child_labour = df['four_four_three'].values[0]
#str
child_labour_str = str(child_labour)
#decision
if(child_labour_str == '1'):
    child_labour_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[3]/fieldset/div/label[1]')
    child_labour_yes.location_once_scrolled_into_view
    child_labour_yes.click()
else:
    child_labour_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[3]/fieldset/div/label[2]')
    child_labour_no.location_once_scrolled_into_view
    child_labour_no.click()

sleep(1)

# 4) Child was sexually abused, defiled, or forced to have sex
sex = df['four_point_four_four'].values[0]
#str
sex_str = str(sex)
#decision
if(sex_str == '1'):
    sex_str_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[4]/fieldset/div/label[1]')
    sex_str_yes.location_once_scrolled_into_view
    sex_str_yes.click()

else:
    sex_str_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[4]/fieldset/div/label[2]')
    sex_str_no.location_once_scrolled_into_view
    sex_str_no.click()

sleep(1)

# 5) The child was stigmatised/ discriminated against due to illness, disability or other reasons
stigma = df['four_point_four_five'].values[0]
#str
stigma_str = str(stigma)
#decision
if(stigma == '1'):
    stigma_str_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[5]/fieldset/div/label[1]')
    stigma_str_yes.location_once_scrolled_into_view
    stigma_str_yes.click()
else:
    stigma_str_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[5]/fieldset/div/label[2]')
    stigma_str_no.location_once_scrolled_into_view
    stigma_str_no.click()

sleep(1)

# Abusive words/ language were used against the child
language = df['four_point_four_six'].values[0]
#str
language_str = str(language)
#decision
if(language_str == '1'):
    language_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[6]/fieldset/div/label[1]')
    language_yes.location_once_scrolled_into_view
    language_yes.click()
else:
    language_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[6]/fieldset/div/label[2]')
    language_no.location_once_scrolled_into_view
    language_no.click()

sleep(1)

# 7) The child has no birth certificate
birth = df['four_point_four_six'].values[0]
#str
birth_str = str(birth)
#decsion
if(birth_str == '1'):
    birth_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[7]/fieldset/div/label[1]')
    birth_yes.location_once_scrolled_into_view
    birth_yes.click()
else:
    birth_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[7]/fieldset/div/label[2]')
    birth_no.location_once_scrolled_into_view
    birth_no.click()

sleep(1)

# 8) The child was in contact/ conflict with the law
law = df['four_point_four_eight'].values[0]
#str
law_str = str(law)
#decision
if(law_str == '1'):
    law_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[8]/fieldset/div/label[1]')
    law_yes.location_once_scrolled_into_view
    law_yes.click()
else:
    law_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[1]/fieldset[8]/fieldset/div/label[2]')
    law_no.location_once_scrolled_into_view
    law_no.click()

sleep(1)

# 4.5. Has the care giver experienced any of these forms f sexual and gender-based violence in the past 6 months?
# 1. Sexual Violence
violence = df['four_point_five_one'].values[0]
#str
violence_str = str(violence)
#decision
if(violence_str == '1'):
    violence_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[1]/fieldset/div/label[1]')
    violence_yes.location_once_scrolled_into_view
    violence_yes.click()
else:
    violence_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[1]/fieldset/div/label[2]')
    violence_no.location_once_scrolled_into_view
    violence_no.click()

sleep(1)

# 2. Physical violence that caused body harm
body_harm = df['four_point_five_two'].values[0]
#str
body_harm_str = str(body_harm)
#decision
if(body_harm_str == '1'):
    body_harm_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[2]/fieldset/div/label[1]')
    body_harm_yes.location_once_scrolled_into_view
    body_harm_yes.click()
else:
    body_harm_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[2]/fieldset/div/label[2]')
    body_harm_no.location_once_scrolled_into_view
    body_harm_no.click()

sleep(1)

# 3. Emotional violence
emotion = df['four_point_five_three'].values[0]
#str
emotion_str = str(emotion)
#decision
if(emotion_str == '1'):
    emotion_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[3]/fieldset/div/label[1]')
    emotion_yes.location_once_scrolled_into_view
    emotion_yes.click()
else:
    emotion_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[3]/fieldset/div/label[2]')
    emotion_no.location_once_scrolled_into_view
    emotion_no.click()

sleep(1)

# 4. Separation
separation = df['four_point_five_four'].values[0]
#str
separation_str = str(separation)
#decision
if(separation_str == '1'):
    separation_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[4]/fieldset/div/label[1]')
    separation_yes.location_once_scrolled_into_view
    separation_yes.click()
else:
    separation_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[4]/fieldset/div/label[2]')
    separation_no.location_once_scrolled_into_view
    separation_no.click()

sleep(1)

# 5. Economic violence
economy = df['four_point_five_four'].values[0]
#str
economy_str = str(economy)
#decision
if(economy_str == '1'):
    economy_yes = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[5]/fieldset/div/label[1]')
    economy_yes.location_once_scrolled_into_view
    economy_yes.click()
else:
    economy_no = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[7]/section[2]/fieldset[5]/fieldset/div/label[2]')
    economy_no.location_once_scrolled_into_view
    economy_no.click()

sleep(1)

# Assessor

assessor = df['service_provider'].values[0]
assessor_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[9]/label[2]/input')
assessor_input.send_keys(assessor)

sleep(1)

assessor_tele =  df['service_provider_tel'].values[0]
assessor_tele_input = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[9]/label[3]/input')
assessor_tele_input.send_keys(str(assessor_tele))


#FIRST CHILL 2.5 ,3.4 ,1.5 ,1.2

#3.1 ,3.2 ,4.1 ,1.3 YES IS 0 

#1.1 Who pays for most of the HH expenses?*
# pull the value from the sheet 
# compare it 
hhspender = df['one_point_one'].values[0]

print(hhspender)
child = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[1]/fieldset/div/label[1]')
grand_parent = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[1]/fieldset/div/label[2]')
other_relative = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[1]/fieldset/div/label[3]')
mother = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[1]/fieldset/div/label[4]')
father = browser.find_element_by_xpath('/html/body/div[1]/article/form/section[4]/fieldset[1]/fieldset/div/label[5]')

if(hhspender == 4 ):
    #thats child 6-17
    child.location_once_scrolled_into_view
    child.click()
elif(hhspender == 3):
    #that's a Grand parent
    grand_parent.location_once_scrolled_into_view
    grand_parent.click()
elif(hhspender == 2):
    #that's the other relative
    other_relative.location_once_scrolled_into_view
    other_relative.click()
elif(hhspender == 1):
    #that's the mother
    mother.location_once_scrolled_into_view
    mother.click()
else:
    #that's the father
    father.location_once_scrolled_into_view
    father.click()

#read push to workedondata sheet
# done_df = pd.read_excel('workedondata.xls', index_col=0)

# #get to know the number of rows
# index = done_df.index

# number_of_rows = len(index)
# print(number_of_rows)

filename = '/home/off-duty-manager/.virtualenvs/automateDataEntry/workedondata.xlsx'
wb = openpyxl.load_workbook(filename=filename)
sheet = wb['Sheet1']
new_row = df.head(1)

sheet.append(new_row.values.tolist())
wb.save(filename)

