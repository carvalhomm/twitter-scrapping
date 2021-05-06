import core as WebBrowserCore

class Controller:
  def __init__(self, browser_name, headless):
    self.browser = WebBrowserCore.WebDriverCore(browser_name, headless)

  def open_url(self, url = ''):
    self.browser.open_url(url)
