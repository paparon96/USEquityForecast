# Import packages
from splinter import Browser
import bs4
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
from selenium.webdriver.support.select import Select
import requests
import urllib.request


# Browser settings
chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options) #options=chrome_options # or empty if we want to see it in action
driver.maximize_window()
#driver = webdriver.Chrome() # or empty if we want to see it in action

driver.get('https://www.multpl.com/shiller-pe/table/by-month')

time.sleep(2)


tbl = driver.find_element_by_xpath("//table[@id='datatable']").get_attribute('outerHTML')

print(tbl)

# Get the data out of the data table
df  = pd.read_html(tbl)[0]

# Rename columns
df.columns = ['Date','CAPE']

print(df.head())

#print(df.columns)

# Export the dataset
df.to_csv('../Data/CAPE_monthly.csv')
