from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from tkinter import *


def search(sh):

    PATH = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.wikipedia.de/")
    search = driver.find_element_by_id("txtSearch")
    search.send_keys(sh)
    search.send_keys(Keys.RETURN)
    main = driver.find_element_by_id("mw-content-text")
    return main.text
    driver.quit()


def click():
    enterd_text=sch.get()
    output.delete(0.0, END)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    PATH = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH, options=option)
    driver.get("https://www.wikipedia.de/")
    search = driver.find_element_by_id("txtSearch")
    search.send_keys(enterd_text)
    search.send_keys(Keys.RETURN)
    #main = driver.find_element_by_id("mw-content-text")
    main = driver.find_element_by_id("content")

    output.insert(END, main.text)

    driver.quit()
    

window = Tk()
window.title("Wiki")
window.configure(background="grey")

Label (window, text="Search Wiki :", bg="grey", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

sch = Entry(window, width=100, bg="lightgrey")
sch.grid(row=2, column=0, sticky=W)

Button(window, text="Search", bg="lightgrey",width=10, command=click) .grid(row=3, column=0, sticky=W)

Label (window, text="Result:", bg="lightgrey", fg="white", font="none 12 bold") .grid(row=5, column=0, sticky=W)

output = Text(window, width=100, height=20, wrap=WORD, background="lightgrey")
output.grid(row=5, column=0, columnspan=2, sticky=W)



window.mainloop()