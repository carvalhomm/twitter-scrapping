import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name, headless):
    self.browser = WebBrowserCore.WebDriverCore(browser_name, headless)

  def open_url(self, url = ''):
    self.browser.open_url(url)
    self.browser.wait_element_visible('div[role="presentation"]')

  def click_on_trend_topics(self, trend):
    element = self.browser.find_element_by('XPATH', '//a[@href="/explore/tabs/'+trend+'"]')
    self.browser.click_on_element(element)

  def search_for(self, text):
    element = self.browser.find_element_by('XPATH', '//input[@data-testid="SearchBox_Search_Input"]')
    self.browser.write_on_element(element, text)
    self.browser.press_key(element, 'ENTER')

  def get_results(self):
    self.browser.wait_element_visible('section[role="region"]')
    html = self.browser.beautify_html()
    timeline = html.find('section', {'role':'region'})
    posts = timeline.find_all('span')
    resultados = []
    for post in posts:
      text = post.getText()
      if len(text) <= 3:
        continue
      resultados.append(text)
    return resultados

    
