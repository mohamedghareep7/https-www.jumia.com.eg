# import requests
# from bs4 import BeautifulSoup


# url = "https://www.jumia.com.eg/electronics/?utm_source=chatgpt.com"
# # print(url)

# respond = requests.get(url)
# print(respond)
# soup = BeautifulSoup(respond.text , "html.parser")
# print(soup)

# continer = soup.find_all("article" , class_="prd _fb _spn c-prd col")
# print(continer)



#====================================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jumia.com.eg/electronics/?utm_source=chatgpt.com")

time.sleep(5)
continer = driver.find_elements(By.CSS_SELECTOR , "article.prd._fb._spn.c-prd.col")
# print(continer)

all_products = []

for item in continer:
    name = item.find_element(By.CLASS_NAME , "name").text
    print('product name :' , name)

    price = item.find_element(By.CLASS_NAME , "prc").text
    print('product price :' , price)

    try :
        discount = item.find_element(By.CSS_SELECTOR , "div.old").text
        print("discount :" , discount)
    except:
        discount = "no discount"
        print("discount :" , discount)

    try:
        discount_percentage = item.find_element(By.CSS_SELECTOR , 'div.bdg._dsct._sm').text
        print("Discount_Percentage :" , discount_percentage) 
    except:
        discount_percentage = '0%' 
        print("discount_percentage :" , discount_percentage ) 
    try:
        rating = item.find_element(By.CSS_SELECTOR , "div.stars._s").text
        print('rating :' , rating)
    except:
        rating = 'no rate'
        print('rating :',rating)

    try:
        number_of_reviews = item.find_element(By.CSS_SELECTOR , 'div.rev').text
        parts = number_of_reviews.split()
        number_of_reviews = parts[4]
        print('Number_of_Reviews :' ,number_of_reviews)
    except:
        number_of_reviews = 'no reviews'
        print('Number_of_Reviews :' , number_of_reviews)

    print("="*20)

    dict_products = {
        "name" : name,
        "product price" : price ,
        "discount" : discount,
        "discount percentage" : discount_percentage,
        "rating" : rating,
        "Number of Reviews" : number_of_reviews
    }

    all_products.append(dict_products)

input("press Enter to close :")
driver.quit()

header = all_products[0].keys()
path = "all products.csv"
with open (path , "w" , encoding="utf-8" , newline="") as file:
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)

