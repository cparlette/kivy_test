from kivy.app import App
from kivy.uix.widget import Widget

class BitflGame(Widget):
	pass

class BitflApp(App):
	def build(self):
		return BitflGame()

if __name__ == '__main__':
	BitflApp().run()