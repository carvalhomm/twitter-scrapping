import PySimpleGUI as sg
import controller

class UserInterface:
  def __init__(self):
    self.window = None
    self.layout = None
    self.controller = None
    self.trending_topics_accepted = ['for-you', 'covid-19', 'trending']

  def generate_layout(self):
    self.layout = [
      [sg.Text('Twitter Scrapping', justification='center', size=(40, 1))],
      [
        sg.Checkbox('Deseja ver a interação com o browser no site do Twitter?', default=False, key='BROWSER_HEADLESS')
      ],
      [
        sg.Text('Pesquisa por Trend Topics', size=(40, 1))
      ],
      [
        sg.Text('(valores aceitos: for-you | covid-19 | trending)', size=(40, 1))
      ],
      [
        sg.Input(size=(40, 1), key='TREND_TOPICS'),
        sg.Button('Pesquisar por Trend Topics'),
      ],
      [sg.Text('Pesquisa por Hashtag (Inclua o "#" na frente)', size=(40, 1))],
      [
        sg.Input(size=(40, 1), key='HASHTAGS'),
        sg.Button('Pesquisar por Hashtags'),
      ],
      [sg.Text('Pesquisa por Palavras Chave', size=(40, 1))],
      [
        sg.Input(size=(40, 1), key='PALAVRAS_CHAVE'),
        sg.Button('Pesquisar por Palavras Chave'),
      ],
      [
        sg.Multiline(size=(40, 10), key="RESULT")
      ]
    ]

  def draw_window(self, title = 'Twitter Scrapping'):
    sg.change_look_and_feel('TanBlue')
    self.window = sg.Window(title, layout=self.layout)

  def instance_browser(self, headless = False):
    self.controller = controller.Controller('chrome', headless)

  def open_twitter(self):
    self.controller.open_url('https://twitter.com/explore')

  def search_trend_topics(self, trends):
    self.controller.click_on_trend_topics(trends)
    return self.controller.get_results()
  
  def search_hashtags(self, hashtags):
    self.controller.search_for(hashtags)
    return self.controller.get_results()

  def search_keywords(self, keywords):
    self.controller.search_for(keywords)
    return self.controller.get_results()

  def wait_for_user_interactions(self):
    user_interacting = True
    while user_interacting == True:
      event, values = self.window.read()
      print('evento --> ', event)
      print('texto --> ', values)
      if event == sg.WIN_CLOSED:
        user_interacting = False
        continue
      browser_headless = bool(values['BROWSER_HEADLESS'])
      if self.controller is None:
        self.instance_browser(not browser_headless)
        self.open_twitter()
      if event == 'Pesquisar por Trend Topics':
        trends = str(values['TREND_TOPICS'].rstrip())
        if trends in self.trending_topics_accepted:
          resultado = self.search_trend_topics(trends)
          self.window['RESULT'].update(resultado)
        else:
          print('valor de trending_topics não aceito')
          self.window['RESULT'].update('valor de trending topics não aceito')
      if event == 'Pesquisar por Hashtags':
        hashtags = str(values['HASHTAGS'].rstrip())
        if '#' in hashtags:
          resultado = self.search_hashtags(hashtags)
          self.window['RESULT'].update(resultado)
        else:
          print('Pesquisa por hashtag está sem #')
          self.window['RESULT'].update('Pesquisa por hashtag está sem #')
      if event == 'Pesquisar por Palavras Chave':
        palavrasChave = str(values['PALAVRAS_CHAVE'].rstrip())
        resultado = self.search_keywords('"' + palavrasChave + '"')
        self.window['RESULT'].update(resultado)
      self.controller.close_browser()
      self.controller = None

    self.window.close()