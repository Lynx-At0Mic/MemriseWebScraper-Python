# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import csv

driver = webdriver.Chrome(r"C:\Users\cabey\Desktop\Program Files\Memrise web scraper\chromedriver webdirver\chromedriver.exe")

def ans(ques):
    ans = False
    csvfile = open('database.csv', 'r')
    reader = csv.reader(csvfile, delimiter=',')
    print("Searching Database...")
    for row in reader:
        if ques == row[0].decode('utf-8'):
            ans = row[1].decode('utf-8')
            print("Answer found!")
            break
        if ques == row[1].decode('utf-8'):
            ans = row[0].decode('utf-8')
            print("Answer found!")
            break
    return(ans)

def startLogin():
    driver.get("https://www.memrise.com/course/1536529/aqa-religious-studies-a")


    uname = driver.find_element_by_xpath("""//*[@id="login"]/div[5]/input""")
    pwd = driver.find_element_by_xpath("""//*[@id="login"]/div[6]/input""")

    print("Logging in...")
    uname.send_keys("Fitness_Gram_Communist")
    pwd.send_keys("fudgeface12")
    pwd.submit()

startLogin()
