#port- 9014

#importing the modules

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#setting up the chrome browser on debugging mode
chrome_driver = r'C:\chromedriver\chromedriver.exe' # directory of the chromedriver.exe
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
driver= webdriver.Chrome(chrome_driver, chrome_options= chrome_options)


site_type = input("4g or 3g\n")

df = pd.read_excel(r"C:\path\to\inputs.xlsx", sheet_name=0)
lst = df['Site Name']
sites = list(lst)
print(sites)



def search():
    search_bar = driver.find_element_by_id('site_name')
    search_bar.send_keys(site)
    search_submit = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[2]')
    search_submit.click()
    edit_button = driver.find_element_by_xpath('//*[@id="content"]/div/form/div[4]/div/a[2]')
    edit_button.click()

def submitting_enodeb():
    enodeb = driver.find_element_by_xpath('//*[@id="id_onair_enodeb"]')
    select_enodeb = Select(enodeb)
    select_enodeb.select_by_value('YES')
    site_submit = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[2]')
    site_submit.click()
    back_to_search = driver.find_element_by_xpath('//*[@id="content"]/div/form/a')
    back_to_search.click()

def submitting_nodeb():
    nodeb = driver.find_element_by_xpath('//*[@id="id_onair_nodeb"]')
    select_nodeb = Select(nodeb)
    select_nodeb.select_by_value('YES')
    site_submit = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[2]')
    site_submit.click()
    back_to_search = driver.find_element_by_xpath('//*[@id="content"]/div/form/a')
    back_to_search.click()






for site in sites:
    search()
    if site_type == '3g':
        submitting_nodeb()
    else:
        submitting_enodeb()





