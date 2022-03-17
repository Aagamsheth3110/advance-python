# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:51:39 2022

@author: AAGAM
"""


import requests           

from bs4 import BeautifulSoup 

import pandas

import argparse

import connect


parser = argparse.ArgumentParser()
parser.add_argument("--dbname", help = "Enter the name of db", type=str)
args = parser.parse_args()


taj_hotel_url = "https://www.tajhotels.com/en-in/taj/taj-exotica-dubai/rooms-and-suites/"
headers = {"Use-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
scraped_info_list = []
connect.connect(args.dbname)


url = taj_hotel_url
print("GET Request for: " +url)
req = requests.get(taj_hotel_url, headers = headers)
content = req.content

soup = BeautifulSoup(content ,"html.parser")

all_hotels = soup.find_all("div", {"class": "rate-card-main-section clearfix"})



for hotel in all_hotels:
    hotel_dict = {}    
    hotel_dict["name"] = hotel.find("h2", {"class": "rate-card-room-heading"}).text
    hotel_dict["description"] = hotel.find("div", {"class": "rate-card-room-description"}).text
    hotel_dict["room_details"] = hotel.find("div", {"class": "row"}).text
    
    
    hotel_dict["pricing"] = hotel.find("div", {"class": "clearfix"}).text
    hotel_dict["actual_price"] = hotel.find("div", {"class": "present-rate"})
    
    scraped_info_list.append(hotel_dict)
    connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
    
    # print(hotel_name,hotel_description,room_details,pricing,actual_price)    
    
dataFrame = pandas.DataFrame(scraped_info_list)
print("data is ending")
dataFrame.to_csv("taj_hotel.csv")
connect.get_hotel_info(args.dbname)













