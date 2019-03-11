import csv
from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

with open('result.csv', 'w') as f:
    f.write("Buyers, Price\n")

driver = webdriver.Chrome("C:\\Users\\Luiz Martini\\"
                          "PycharmProjects\\PythonChallenges"
                          "\\drivers\\chromedriver.exe")

for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)

    buyers = driver.find_elements_by_xpath("//div[@title='buyer-name']")
    prices = driver.find_elements_by_xpath("//span[@class='item-price']")

    num_page_items = len(buyers)
    with open("results.csv", "a") as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.quit()
