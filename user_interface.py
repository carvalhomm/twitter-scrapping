import PySimpleGUI as sg
import controller

class UserInterface:
  def __init__(self):
    self.window = None
    self.layout = None
    self.controller = None
    self.trending_topics_accepted = ['for-you', 'covid-19', 'trending', 'news_unified', 'sports_unified', 'entertainment_unified']

  def generate_layout(self):
    self.layout = [
      [sg.Text('Twitter Scrapping', justification='center', size=(40, 1))],
      [
        sg.Checkbox('Deseja ver a interação com o browser no site do Twitter?', default=False, key='BROWSER_HEADLESS')
      ],
      [
        sg.Text('Limite de Resultados (O limite é 30)', size=(40, 1)),
        sg.Multiline(size=(5, 1), enter_submits=False, key='QUANTIDADE', do_not_clear=False)
      ],
      [sg.Text('Pesquisa por Trend Topics (valores aceitos: for-you | covid-19 | trending | news_unified | sports_unified | entertainment_unified)', size=(40, 1))],
      [
        sg.Multiline(size=(10, 1), enter_submits=False, key='TREND_TOPICS', do_not_clear=False),
        sg.Button('Pesquisar por Trend Topics', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ],
      [sg.Text('Pesquisa por Hashtag (Inclua o "#" na frente)', size=(40, 1))],
      [
        sg.Multiline(size=(10, 1), enter_submits=False, key='HASHTAGS', do_not_clear=False),
        sg.Button('Pesquisar por Hashtags', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ],
      [sg.Text('Pesquisa por Palavras Chave', size=(40, 1))],
      [
        sg.Multiline(size=(10, 1), enter_submits=False, key='PALAVRAS_CHAVE', do_not_clear=False),
        sg.Button('Pesquisar por Palavras Chave', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ]
    ]

  def draw_window(self, title = 'Twitter Scrapping'):
    sg.theme('reddit')
    self.window = sg.Window(title, layout=self.layout, default_button_element_size=(8,2), use_default_focus=False)

  def instance_browser(self, headless = False):
    self.controller = controller.Controller('chrome', headless)

  def interact_with_browser(self):
    self.controller.open_url('https://twitter.com/explore')

  def search_trend_topics(self, trends, quantidade):
    self.controller.open_url()
  
  def search_hashtags(self, hashtags, quantidade):
    self.controller.open_url()

  def search_keywords(self, keywords, quantidade):
    self.controller

  def wait_for_user_interactions(self):
    user_interacting = True
    while user_interacting == True:
      event, values = self.window.read()
      print('evento --> ', event)
      print('texto --> ', values)
      if event == sg.WIN_CLOSED:
        user_interacting = False
        continue
      quantidade = int(values['QUANTIDADE'].rstrip())
      browser_headless = bool(values['BROWSER_HEADLESS'])
      self.instance_browser(browser_headless)
      self.interact_with_browser()
      if event == 'Pesquisa por Trend Topics':
        trends = str(values['TREND_TOPICS'].rstrip()).trim()
        if trends in trending_topics_accepted:
          self.search_trend_topics(trends, quantidade)
        else:
          print('valor de trending_topics não aceito')
      if event == 'Pesquisar por Hashtags':
        hashtags = str(values['HASHTAGS'].rstrip()).trim()
        if '#' in hashtags:
          self.search_hashtags(hashtags, quantidade)
        else:
          print('Pesquisa por hashtag está sem #')
      if event == 'Pesquisar por Palavras Chave':
        palavrasChave = str(values['PALAVRAS_CHAVE'].rstrip()).trim()
        self.search_keywords('"' + palavrasChave + '"', quantidade)

    self.window.close()