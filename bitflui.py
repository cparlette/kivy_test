from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class Selector(FloatLayout):
    app = ObjectProperty(None)


class bitfluiApp(App):

    def build(self):
        self.root = FloatLayout()
        self.selector = Selector(app=self)
        self.root.add_widget(self.selector)
        return self.root


bitfluiApp().run()
