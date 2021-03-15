from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
class WebDriverCore:
  def __init__(self, browser_name):
    self.driver = self.create_webdriver(browser_name)
    self.wait = WebDriverWait(self.driver, 10)

  def create_webdriver(self, browser_name = 'chrome'):
    try:
      if browser_name == 'chrome':
        return webdriver.Chrome()
      elif browser_name == 'firefox':
        return webdriver.Firefox()
      elif browser_name == 'edge':
        return webdriver.Edge()
      return None
    except error:
      print(error)
      return None

  def wait_text_element(self, method = 'ID', selector, value):
    if self.wait is None or value is None or selector is None:
      return None
    method = method.upper()
    self.wait.until(EC.text_to_be_present_in_element((getattr(By, method), selector), value))

  def wait_element_invisible(self, method = 'ID', value):
    if self.wait is None or value is None:
      return None
    method = method.upper()
    self.wait.until(EC.invisibility_of_element_located(getattr(By, method), value))

  def wait_element_visible(self, method = 'ID', value):
    if self.wait is None or value is None:
      return None
    method = method.upper()
    self.wait.until(EC.visibility_of(getattr(By, method), value))

  def find_element_by(self, method = 'ID', value):
    if self.driver is None or value is None:
      return None
    method = method.upper()
    return self.driver.find_element(getattr(By, method), value)

  def find_elements_by(self, method = 'ID', value):
    if self.driver is None or value is None:
      return None
    method = method.upper()
    return self.driver.find_elements(getattr(By, method), value)

  def click_on_element(self, element):
    if self.driver is None or element is None:
      return
    element.click()

  def press_key(self, element, key='ENTER'):
    if self.driver is None or element is None:
      return
    element.send_keys(getattr(Keys, key))
  
  def write_on_element(self, element, value = ''):
    if self.driver is None or element is None:
      return
    element.send_keys(value)

  def open_url(self, url):
    if self.driver is None:
      return
    self.driver.get(url)

  def beautify_html(self):
    if self.driver is None:
      return None
    return BeautifulSoup(self.driver.page_source, 'html.parser')

  def close_browser(self):
    if self.driver is not None:
      self.driver.close()
    return True