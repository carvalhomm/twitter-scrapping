import PySimpleGUI as sg
import controller

class UserInterface:
  def __init__():
    self.window = None
    self.layout = None
    self.controller = controller.Controller('chrome', False)

  def generate_layout(self):
    self.layout = [
      [sg.Text('Twitter Scrapping', size=(40, 1))],
      [
        sg.Text('Quantidade de resultados (O limite é 30)', size=(40, 1)),
        sg.Multiline(size=(70, 5), enter_submits=False, key='QUANTIDADE', do_not_clear=False)
      ]
      [sg.Text('Pesquisa por Trend Topics', size=(40, 1))],
      [
        sg.Multiline(size=(70, 5), enter_submits=False, key='TREND_TOPICS', do_not_clear=False),
        sg.Button('Pesquisar por Trend Topics', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ],
      [sg.Text('Pesquisa por Hashtag (Pode ser mais de uma, separados por um espaço simples)', size=(40, 1))],
      [
        sg.Multiline(size=(70, 5), enter_submits=False, key='HASHTAGS', do_not_clear=False),
        sg.Button('Pesquisar por Hashtags', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ],
      [sg.Text('Pesquisa por Palavras Chave', size=(40, 1))],
      [
        sg.Multiline(size=(70, 5), enter_submits=False, key='PALAVRAS_CHAVE', do_not_clear=False),
        sg.Button('Pesquisar por Palavras Chave', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
      ]
    ]

  def draw_window(self, title = 'Twitter Scrapping'):
    self.window = sg.Window(title, layout=self.layout)

  def wait_for_user_interactions(self):
    user_interacting = True
    while user_interacting == True:
      event, values = self.window.read()
      print('evento --> ', event)
      print('texto --> ', values)
      if event in (sg.WIN_CLOSED, 'EXIT'):
        user_interacting = False

    self.window.close()

  def interact_with_browser(self):
    self.controller.open_url('https://twitter.com/explore')