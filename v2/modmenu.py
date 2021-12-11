import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (400, 600)

class window_widget(Widget):
	def __init__(self, **kwargs):
		super(window_widget, self).__init__(**kwargs)

		reload = Button(text ='RELOAD',
				font_size ="15sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				size=(250,175),
				pos=(75,400))
		reload.bind(on_press = self.rehack)
		self.add_widget(reload)

		hckdir = TextInput(hint_text ='Enter the path for Asset Indexer',
				font_size ="15sp",
                size=(175, 40),
                pos=(75, 375))
		self.add_widget(hckdir)

		brwse = Button(text ='Browse',
				font_size ="15sp",
				background_color =(1, 1, 1, 1),
				color =(1, 1, 1, 1),
				size=(75, 40),
				pos=(250, 375))
		self.add_widget(brwse)
	def rehack(self, instance):
		print("Button is pressed")


# create App class
class modmenu(App):

	def build(self):
		return window_widget()

if __name__ == "__main__":
	modmenu().run()
