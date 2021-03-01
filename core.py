from selenium import webdriver
from bs4 import BeautifulSoup

def create_webdriver(type):
  if type == 'chrome':
    return webdriver.Chrome()
  elif type == 'firefox':
    return webdriver.Firefox()
  elif type == 'edge':
    return webdriver.Edge()
  return None

def beautify_html(html):
  return BeautifulSoup(html, 'html.parser')
