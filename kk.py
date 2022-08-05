from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from scrapy import Selector
import time
import json
PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
j=0
Data_liste=[]
xpath_liste=[]
for i in range(1,5):
    driver.get("https://www.accuweather.com/fr/world-weather")
    response = Selector(text=driver.page_source)
    time.sleep(4)
    elem = response.xpath("/html/body/div/div[4]/div[1]/div[1]/div[1]/div")
    noms=response.xpath("//a["+str(i)+"]/span[1]/text()").get()
    #noms.click()
    response.xpath( "//a["+str(i)+"]/@href").click()

    #url = response.xpath('//a["+str(i)+"]/@href').getall()
    #xpath_liste.append(url)
    #for urls in xpath_liste:
      #  driver.get(urls[j])
      #  response = Selector(text=driver.page_source)
      #  Qualité_air1 = response.xpath('/a[1]/div[1]/div[2]/div[2]/span[2]').get()
    dictionary = {
        'nom': noms,
      #  'Qualité_air': Qualité_air1,
    }
    Data_liste.append(dictionary)
    time.sleep(3)
    with open("DC.json", "w") as outfile:
        json.dump(Data_liste, outfile)



#xpath_liste=[]
#for i in range(1,5):

#    response1 = Selector(text=driver.page_source)
#    time.sleep(4)
#    elem = response1.xpath('/html/body/div/div[4]/div[1]/div/div[1]/div')
#    city1=response1.xpath('//a['+str(i)+']/span[1]/text()').get()
#    city1.click()
#    driver.find_element_by_id("submit").click()
#    response1.xpath('/html/body/div/div[4]/div[1]/div/div[1]/div/a[1]').click()
#    url = response1.xpath('//a[' + str(i) + ']/@href').getall()
#   xpath_liste.append(url)
#   for urls in xpath_liste:
#       driver.get(urls[j])
#        response = Selector(text=driver.page_source)
#        elem = response.xpath('/html/body/div/div[5]/div[1]/div[1]').get()
#        meteo_actuelle1=response.xpath('//a[1]/div[1]/div[1]/div/div/div[1]').get()
#        cette_nuit1=response.xpath('//div[5]/a/div[2]/div[1]/div/div[1]').get()
#        Demain1=response.xpath('//div[6]/a/div[2]/div[1]/div/div[1]').get()
#       Qualité_air1=response.xpath('/a[1]/div[1]/div[2]/div[2]/span[2]').get()
#        vent1=response.xpath('/a[1]/div[1]/div[2]/div[3]/span[2]').get()
    #url = response.xpath('//a[' + str(i) + ']').click()
#    time.sleep(10)

   # dictionary = {
    #          'nom': noms,
    #         'meteo_actuelle': meteo_actuelle1,
    #         'cette_nuit': cette_nuit1,
    #         'Demain': Demain  1,
    #         'Qualité_air': Qualité_air1,
    #         'vent': vent1
    #    }
    #   j = j + 1
    #Data_liste.append(dictionary)
    #time.sleep(3)
    #with open("DC.json", "w") as outfile:
     #json.dump(Data_liste, outfile)
#print(noms)
#elem = response.xpath('//*[@id="ResultsContainer"]')