from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.toast import toast
from kivymd.app import MDApp

KV = '''
MDScreen:

    MDFlatButton:       
        text: "My Toast"
        pos_hint:{"center_x": .5, "center_y": .5}
        on_press: app.show_toast()
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_toast(self):
        toast("Hello World", True, 80, 200, 0)


Test().run()