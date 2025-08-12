from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")
time.sleep(2)

with open("flipkart_watches.txt", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

serch_bar=driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
input_query=serch_bar.send_keys("Watches for Men under 2000"+Keys.RETURN)
time.sleep(5)
w_d=driver.find_elements(By.XPATH, "//div[@class='hCKiGj']")

name=driver.find_elements(By.CLASS_NAME,"WKTcLC")
brand=driver.find_elements(By.CLASS_NAME,"syl9yP")
price=driver.find_elements(By.CLASS_NAME,"Nx9bqj")

data = []
for n ,b,p  in zip(name,brand,price):
    data.append([n.text, b.text, p.text,"In Stock"])
    print(f"Name: {n.text}, Brand: {b.text}, Price: {p.text}")

df = pd.DataFrame(data, columns=["Name", "Brand", "Price","Availability"])
df.to_excel("Watches_data.xlsx", index=False)
time.sleep(3)
driver.quit()
