import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name, headless):
    self.browser = WebBrowserCore.WebDriverCore(browser_name, headless)

  def open_url(self, url = ''):
    self.browser.open_url(url)
    print('url open')
    self.browser.wait_element_presence('//div[@role="tablist"]')
    # self.browser.wait_element_visible('//div[@role="tablist"]')

  def click_on_trend_topics(self, trend):
    element = self.browser.find_element_by('XPATH', '//a[@href="/explore/tabs/'+url+'"]')
    self.browser.click_on_element(element)

  def search_for(self, text):
    element = self.browser.find_element_by('XPATH', '//input[@data-testid="SearchBox_Search_Input"]')
    self.browser.write_on_element(element, text)
    self.browser.press_key(element, 'ENTER')

  def get_results(self):
    print('getting results')
    self.browser.wait_element_presence('//div[@aria-label="Timeline: Buscar timeline"]')
    # self.browser.wait_element_visible('//div[@aria-label="Timeline: Buscar timeline"]')
    html = self.browser.beautify_html()
    timeline = html.find('//div[@aria-label="Timeline: Buscar timeline"]')
    posts = timeline.find_all('article')
    print('posts --> ', posts)
    
