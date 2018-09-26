from kivy.app import App
from kivy.uix.label import Label


class Application(App):
    def build(self):
        lbl=Label(text='Hello World!', font_size="70sp")
        return lbl

if __name__ == '__main__':
    Application().run()