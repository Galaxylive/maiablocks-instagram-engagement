from tkinter import *
import threading
import sys
import codecs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import datetime
import pywintypes
import win32gui
import win32con
hwnd = win32gui.GetForegroundWindow()
win32gui.MoveWindow(hwnd, 341, 0, 700, 320, True)
clear = lambda: os.system('cls')
title = lambda: os.system('title MAIA: Console')
color = lambda: os.system('color F0')
exit = lambda: os.system('exit')
clear()
title()
color()
def timecount(totalwait):
    time_check = 0
    time_total = totalwait
    while time_check < time_total:
        sleep(1)
        print("Waiting: " + str(time_check + 1) + " Sec.")
        time_check = time_check + 1
        if time_total == time_check:
            print("Waiting Complete.")
def doengagement(username, password, hashtag, limit):
    eng_button = Button(cv, text=" MAIA is Working ", state="disable", bg="#00c2cb", command=threading.Thread(target=lambda: doengagement(entry_username.get(), entry_password.get(), entry_hashtag.get(), entry_limit.get())).start)
    eng_button.grid(row=2, column=0, columnspan=3, pady=20)
    status_label.config(text="Please wait, MAIA is Working", bg="#c1c6cc")
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.set_window_position(900, 0)
    driver.set_window_size(200, 900)
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    timecount(2)
    print("Handling Cookies.")
    driver.find_element_by_xpath("//html/body/div[2]/div/div/div/div[2]/button[1]").click()
    timecount(2)
    userLogin = driver.find_element_by_name('username')
    userHashtag = str(hashtag)
    userLogin.send_keys(username)
    print("Handling Username.")
    status_label.config(text="Handling Username")
    passLogin = driver.find_element_by_name('password')
    passLogin.send_keys(password)
    print("Handling Password.")
    status_label.config(text="Handling Password")
    submit = driver.find_element_by_tag_name('form')
    submit.submit()
    status_label.config(text="Accessing Instagram")
    print("Accessing Instagram.")
    timecount(5) 
    driver.get("https://instagram.com/explore/tags/" + userHashtag)
    print("Opening Hashtag #" + userHashtag + ".")
    print("https://instagram.com/explore/tags/" + userHashtag)
    status_label.config(text="Opening Hashtag: #" + userHashtag)
    sleep(10)
    driver.find_element_by_xpath("//a[contains(@href, '/p/')]").click()
    print("Starting Engagement.\n")
    timecount(3)
    print("---------------------------------------------------------")
    engagements = 0
    engLimit = int(limit)
    while engagements != engLimit:
        if engagements < engLimit:
            try:
                try:
                    profile = driver.find_element_by_xpath("//html/body/div/div/div/article/header/div/div/div/span/a").text
                    profile_url = driver.current_url
                    date_time = datetime.datetime.now()
                    NULL_ = None
                    driver.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]').click()
                    engDisplay = engagements + 1
                    status_label.config(text="Enganging with: @" + profile + " - " + str(engDisplay) + "/" + limit)
                    print("Starting Engagement: " + str(engDisplay) + "/" + limit)
                    timecount(1)
                    print("#########################################################")
                    print("Profile: " + profile)
                    print("URL: " + profile_url)
                    print("Date: " + str(date_time.date()))
                    print("Time: " + str(date_time.strftime("%X")))
                    print("#########################################################")
                    try:
                        try:
                            driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                        except:
                            driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                    except ElementClickInterceptedException:
                        print("WARNING: Interaction intercepted by Instagram.")
                        status_label.config(text="WARNING: Interaction intercepted by Instagram.")
                        print("Closing Application, please try again later.")
                        timecount(10)
                        print("Disconnecting Driver")
                        status_label.config(text="Disconnecting Chrome Driver")
                        driver.close()
                        timecount(3)
                        print("Disconnecting Database")
                        status_label.config(text="Disconnecting Database")
                        timecount(3)
                        print("Closing MAIA User Interface")
                        status_label.config(text="Closing MAIA Interface")
                        timecount(5)
                        root.destroy()
                        timecount(3)
                        print("EXECUTING KILL COMMAND")
                        timecount(3)
                        exit()
                        win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
                        timecount(100)
                    print("Completing Engagement.")
                    timecount(3)
                    print("Engagement Complete.")
                    print("---------------------------------------------------------")
                    engagements += 1
                except ElementNotInteractableException:
                    try:
                        driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                    except:
                        driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                    print("Post already liked: Moving to the next.")
                    timecount(3)
                    print("Complete.")
                    print("---------------------------------------------------------")
            except NoSuchElementException:
                try:
                    driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a[2]").click()
                except:
                    driver.find_element_by_xpath("//html/body/div[5]/div[1]/div/div/a").click()
                print("Post already liked: Moving to the next. -- NSElement")
                timecount(3)
                print("Complete.")
                print("---------------------------------------------------------")
    else:
        status_label.config(text="www.maiablocks.com", bg="#f4f6fc")
        eng_button = Button(cv, text="Start Engagement", command=threading.Thread(target=lambda: doengagement(entry_username.get(), entry_password.get(), entry_hashtag.get(), entry_limit.get())).start)
        eng_button.grid(row=2, column=0, columnspan=3, pady=20)
        print("\nEngagement Function Complete.")
        timecount(1)
        print("Disconnecting from MAIA Database")
        timecount(1)
        print("Closing Browser.")
        driver.close()
root = Tk()
def forget(widget):
    widget.grid_forget()
root.title("MAIA: Instagram Engagement")
root.geometry("340x280+0+0")
root.iconbitmap("./images/maia_icon2.ico")
root.resizable(False,False)
global userLogin
global userHashtag
global mycursor
global mydb
print("#########################################################")
print("#               MAIA Blocks - FBI 1.0.1                 #")
print("#########################################################")
cv = Canvas(root, width=340, height=280)
cv.pack(side='top', fill='both', expand='yes')
bg_file = "./images/insta_proto01.gif"
bg_image = PhotoImage(file=bg_file)
cv.create_image(0, 0, image=bg_image, anchor='nw')
cv.create_text(10, 100, text="#Hashtagh", fill="black", anchor='nw')
cv.create_text(230, 100, text="Engagement Limit", fill="black", anchor='nw')
entry_hashtag = Entry(cv, width=32)
entry_hashtag.grid(row=0, column=0, columnspan=2, padx=10, pady=(120,0), sticky="W")
entry_limit = Entry(cv, width=16)
entry_limit.grid(row=0, column=1, padx=(56,0),pady=(120,0), sticky="W")
cv.create_text(10, 150, text="Username", fill="black", anchor='nw')
entry_username = Entry(cv, width=25)
entry_username.grid(row=1, column=0, padx=10, pady=(30,0), sticky="W")
cv.create_text(177, 150, text="Password", fill="black", anchor='nw')
entry_password = Entry(cv, width=25, show="*")
entry_password.grid(row=1, column=1, padx=(2,0), pady=(30,0), sticky="W")
eng_button = Button(cv, text="Start Engagement", command=threading.Thread(target=lambda: doengagement(entry_username.get(), entry_password.get(), entry_hashtag.get(), entry_limit.get())).start)
eng_button.grid(row=2, column=0, columnspan=3, pady=20)
status_label = Label(root, text="www.maiablocks.com", width=340, bg="#f4f6fc")
status_label.pack()
root.mainloop()