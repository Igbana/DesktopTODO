from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class HomePage(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        return HomePage()

MainApp().run()