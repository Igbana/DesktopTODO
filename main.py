from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivy.metrics import dp

class HomePage(MDScreen):
    def new_task(self):
        anim = Animation()
        # anim.start()
        self.add_btn.a = 90
        self.add_btn.b = 270
        self.add_btn.canvas.ask_update()
        self.new_card = NewTaskCard(y = self.add_btn.pos[1]+dp(31), pos_hint = {'center_x': 0.5})
        self.add_widget(self.new_card, index = 1)
        self.add_btn.icon = 'check'
        # self.add_btn.on_release = lambda: self.add_task()
        print('Done')

    def text_actions(self):
        pass
    
    def add_task(self):
        self.remove_widget(self.new_card)
        self.add_btn.a = 0
        self.add_btn.b = 360
        self.add_btn.icon = 'plus'
        self.add_btn.canvas.ask_update()
        self.add_btn.on_release = self.new_task
        print("Added")

class NewTaskCard(MDCard):
    pass

class MainApp(MDApp):
    def build(self):
        return HomePage()

MainApp().run()