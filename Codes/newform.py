# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 16:32:19 2018

@author: Iswarya
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd 
lat=[]
lon=[]
df=pd.read_csv('F:/WaterCsv/bak_coords.csv')
driver = webdriver.Chrome()
driver.get('https://www.whoi.edu/marine/ndsf/cgi-bin/NDSFutility.cgi?form=0&from=XY&to=LatLon')
for index,row in df.iterrows():
    
    Xcord = driver.find_element_by_name("Xcord")
    Ycord = driver.find_element_by_name("Ycord")
    LatDeg = driver.find_element_by_name("LatDeg")
    LatMin = driver.find_element_by_name("LatMin")
    LonDeg = driver.find_element_by_name("LonDeg")
    LonMin = driver.find_element_by_name("LonMin")
    Xcord.send_keys(str(row['latitude']*500))
    Ycord.send_keys(str(row['longitude']*500))
    LatDeg.send_keys("34")
    LatMin.send_keys("3")
    LonDeg.send_keys("118")
    LonMin.send_keys("14")
    convert = driver.find_element_by_xpath("/html/body/form/h2[2]/p/input[1]")
    convert.click()
    lt = driver.find_element_by_name("DecSLat")
    ln = driver.find_element_by_name("DecSLon")
    lat.append(lt.get_attribute("value"))
    lon.append(ln.get_attribute("value"))
    reset = driver.find_element_by_xpath("/html/body/form/h2[2]/p/input[2]")
    reset.click()
    
mydf3 = pd.DataFrame(
    {'Id': df['Id'],
     'latitude': lat,
     'longitude': lon
    })
#print(mydf3)
#writer = pd.ExcelWriter('C:/Users/Iswarya/Documents/test.xlsx')
mydf3.to_csv('C:/Users/Iswarya/Documents/bak_latlon.csv')
