import csv
from selenium import webdriver

MAX_PAGE_NUM = 5  # Número de páginas a serem raspadas.
MAX_PAGE_DIG = 3  # Quantidade de digitos para url da página.

with open('result.csv', 'w') as f:
    f.write("Buyers, Price\n")

driver = webdriver.Chrome()  # Inicia o navegador.

for i in range(1, MAX_PAGE_NUM + 1):  # Muda a url para automatizar o processo.
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)  # Acessa a url

    buyers = driver.find_elements_by_xpath("//div[@title='buyer-name']")  # Identifica e seleciona algum elemento.
    prices = driver.find_elements_by_xpath("//span[@class='item-price']")  # Identifica e seleciona algum elemento.

    num_page_items = len(buyers)  # Quantidade de elementos.

#  Escreve os dados retirados do site em um arquivo .csv
    with open("results.csv", "a") as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

#  Encerra o driver do navegador e fecha a janela.
driver.quit()
