# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import csv


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
    driver.get("https://www.memrise.com/course/1536529/aqa-religious-studies-a/garden/speed_review/")


    uname = driver.find_element_by_xpath("""//*[@id="login"]/div[5]/input""")
    pwd = driver.find_element_by_xpath("""//*[@id="login"]/div[6]/input""")

    print("Logging in...")
    uname.send_keys("Fitness_Gram_Communist")
    pwd.send_keys("fudgeface12")
    pwd.submit()

driver = webdriver.Chrome(r"C:\Users\cabey\Desktop\Program Files\Memrise web scraper\chromedriver webdirver\chromedriver.exe")

startLogin()

while True:
    sleep(5)
    while True:
        counter = 0
        ques = driver.find_element_by_xpath("""//*[@id="boxes"]/div/div[1]/div[2]""").text
        crans = ans(ques)
        mc1 = driver.find_element_by_xpath("""//*[@id="boxes"]/div/ol/li[1]/span[2]""")
        mc2 = driver.find_element_by_xpath("""//*[@id="boxes"]/div/ol/li[2]/span[2]""")
        mc3 = driver.find_element_by_xpath("""//*[@id="boxes"]/div/ol/li[3]/span[2]""")
        mc4 = driver.find_element_by_xpath("""//*[@id="boxes"]/div/ol/li[4]/span[2]""")

        if crans == False:
            print("Unkown question: " + ques)
            print("Possible answers:")
            print mc1.text
            print mc2.text
            print mc3.text
            print mc4.text
            print("\n" * 5)
            counter = 7
            #driver.quit()
            #break

        elif crans == mc1.text:
            mc1.click()
            print("Correct answer, BOX1\nMoving mouse...\nClicked!\n")
        elif crans == mc2.text:
            mc2.click()
            print("Correct answer, BOX2\nMoving mouse...\nClicked!\n")
        elif crans == mc3.text:
            mc3.click()
            print("Correct answer, BOX3\nMoving mouse...\nClicked!\n")
        elif crans == mc4.text:
            mc4.click()
            print("Correct answer, BOX4\nMoving mouse...\nClicked!\n")

        else:
            print("Answres in database do not match given!: " + ques)
            print("Answer in database:" + crans)
            print("Possible answers:")
            print mc1.text
            print mc2.text
            print mc3.text
            print mc4.text
            print("\n" * 5)
            counter = 7
            #driver.quit()
            #break
        while ques == driver.find_element_by_xpath("""//*[@id="boxes"]/div/div[1]/div[2]""").text and counter != 6:
            sleep(0.5)
            counter = counter + 1
        if counter == 6:
            print("Restart...")
            break
        else:
            continue
        
    driver.find_element_by_xpath("""/html/body/div[4]/div/button""").click()
    driver.get("https://www.memrise.com/course/1536529/aqa-religious-studies-a/garden/speed_review/")
