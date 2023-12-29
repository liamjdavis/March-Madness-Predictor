from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import mysql.connector
from mysql.connector import Error

import time

# open driver
driver = webdriver.Chrome()

url = "https://www.espn.com/mens-college-basketball/stats/team"
driver.get(url)

# sleep to give time to load
wait = WebDriverWait(driver, 5)

# find rows in table
table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".responsive-table")))
rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

# set up MySQL connection
try:
    connection = mysql.connector.connect()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")