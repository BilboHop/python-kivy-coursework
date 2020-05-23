from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        return Button(text='Hello world')

if __name__ == '_main_':
    MyApp().run()
