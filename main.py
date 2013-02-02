from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty

class BitflGame(FloatLayout):
    label_wid = ObjectProperty()
    info = StringProperty()
    
    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'

class BitflApp(App):
	def build(self):
		return BitflGame(info="Hello, World")

if __name__ == '__main__':
	BitflApp().run()