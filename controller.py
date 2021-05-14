import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name, headless):
    self.browser = WebBrowserCore.WebDriverCore(browser_name, headless)
    self.browser.driver.set_window_size(900, 745)

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
    resultado = ''
    for post in posts:
      text = post.getText()
      if len(text) <= 3:
        continue
      if 'Assunto' in text:
        continue
      if 'Tweets' in text:
        continue
      if 'Seguir' in text:
        continue
      resultado = resultado + text + '\n'
    return resultado
  
  def close_browser(self):
    self.browser.close_browser()
    self.browser = None

    
