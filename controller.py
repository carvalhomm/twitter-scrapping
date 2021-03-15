import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name):
    self.browser = WebBrowserCore(browser_name)

  def search_for(self, url = '', input):
    self.browser.open_url(url)
    self.browser