
from curses import window
from lib2to3.pgen2 import driver
from re import search
from unicodedata import name
import webbrowser
import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

browser = webdriver.Chrome(options=chrome_options)
browser.execute_script("window.open('https://www.thecommunitylibraryproject.org/books/bookshelf/picture-books/');")

title = browser.find_element_by_class_name('oxy-post-title-hindi')

print(title)
	 


