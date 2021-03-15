import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name, headless):
    self.browser = WebBrowserCore.WebDriverCore(browser_name, headless)

  def search_for(self, url = '', text = ''):
    self.browser.open_url(url)
    self.browser.wait_element_visible('#search_query')
    element = self.browser.find_element_by('ID', 'search_query')
    self.browser.write_on_element(element, text)
    self.browser.press_key(element, 'ENTER')
