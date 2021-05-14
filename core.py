from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from bs4 import BeautifulSoup

class WebDriverCore:
  def __init__(self, browser_name, headless):
    self.driver = self.create_webdriver(browser_name, headless)
    self.wait = WebDriverWait(self.driver, 30)

  def create_webdriver(self, browser_name = 'chrome', headless = False):
    try:
      if browser_name == 'chrome':
        chrome_options = Options()
        if headless is True:
          chrome_options.add_argument('--headless')
          chrome_options.add_argument('--no-sandbox')
          chrome_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())
      elif browser_name == 'firefox':
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
      elif browser_name == 'edge':
        return webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
      return None
    except:
      print('error instancing driver')
      return None

  def sleep_driver(self, seconds = 5):
    time.sleep(seconds)

  def wait_text_element(self, selector = None, value = None):
    if self.wait is None or value is None or selector is None:
      return None
    self.wait.until(EC.text_to_be_present_in_element(selector, value))

  def wait_element_invisible(self, value = None):
    if self.wait is None or value is None:
      return None
    self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, value)))

  def scroll_page(self):
    if self.driver is None:
      return
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  def wait_element_presence(self, value = None):
    if self.driver is None or value is None:
      return
    self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))

  def wait_element_visible(self, value = None):
    if self.wait is None or value is None:
      return None
    self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))

  def find_element_by(self, method = 'ID', value = None):
    if self.driver is None or value is None:
      return None
    method = method.upper()
    return self.driver.find_element(getattr(By, method), value)

  def find_elements_by(self, method = 'ID', value = None):
    if self.driver is None or value is None:
      return None
    method = method.upper()
    return self.driver.find_elements(getattr(By, method), value)

  def click_on_element(self, element):
    if self.driver is None or element is None:
      return
    element.click()

  def press_key(self, element = None, key = 'ENTER'):
    if self.driver is None or element is None:
      return
    element.send_keys(getattr(Keys, key))
  
  def write_on_element(self, element = None, value = ''):
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
      self.driver = None
      self.wait = None
    return True
