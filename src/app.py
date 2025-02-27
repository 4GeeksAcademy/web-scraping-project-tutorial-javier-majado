# import os
# from bs4 import BeautifulSoup
# import requests
# import time
# import sqlite3
# import matplotlib.pyplot as plt
# import seaborn as sns

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)

URL = "https://companies-market-cap-copy.vercel.app/index.html"
driver.get(URL)
table = driver.find_element(By.CLASS_NAME, "table")
for t in table:
    print(t.text)
list_td =[]
for row in table.find_elements(By.CSS_SELECTOR, "tbody tr"):
    #print(row.text)
    #for data in row.find_elements(By.TAG_NAME, "td"):
        #print(data.text)
    celdas = row.find_elements(By.CSS_SELECTOR, 'td')
    list_td.append([celda.text for celda in celdas])
list_head = []
for row in table.find_elements(By.CSS_SELECTOR, "thead tr"):
    celdas = row.find_elements(By.CSS_SELECTOR, 'th')
    list_head.append([celda.text for celda in celdas])
dataframe = pd.DataFrame(list_td, columns =list_head )
dataframe.drop('Change', axis=1, inplace=True)
dataframe["Revenue"]= dataframe["Revenue"].str.replace("B","").astype(float)
#dataframe= dataframe.dropna()
print(dataframe)


