# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 15:19:54 2018

@author: Iswarya
"""

import urllib3
# from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
from bs4 import BeautifulSoup
import pandas as pd 

df=pd.read_csv('C:/Users/Iswarya/Documents/coords.csv')

from robobrowser import RoboBrowser
browser = RoboBrowser(history=True)
browser.open('https://www.whoi.edu/marine/ndsf/cgi-bin/NDSFutility.cgi?form=0&from=XY&to=LatLon')
df["latitude"]=df["latitude"].astype(int)
df["longitude"]=df["longitude"].astype(int)

form = browser.get_forms()[0]
form["Xcord"].value="514.25"
form['Ycord'].value=282.74
form['LatDeg'].value=30
form['LatMin'].value=15
form['LonDeg'].value=120
form['LonMin'].value=10
#form = browser.submit_form(form)
form = browser.follow_link="xy2ll(document.XY2LLForm)"
print(form)
print(form["DecSLat"].value)
# Now you can fill each elements in form as given below