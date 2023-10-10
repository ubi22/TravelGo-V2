import sqlite3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
import requests
import json
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.button import MDRaisedButton
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCardSwipe
import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.animation import Animation
from kivy.factory import Factory
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineIconListItem
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.core.window import Window
import sqlite3
import hashlib
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivymd.uix.list import MDList
from kivymd import images_path
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivymd.uix.button import MDTextButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.factory import Factory
from kivymd.uix.button import MDIconButton
from bs4 import BeautifulSoup
import requests
import sqlite3
from kivy.core.text import LabelBase
import time
from kivymd.toast import toast
Window.size = (480, 800)
API = '6c39b074-59ea-4ce3-8924-c1b26f5e9137'

def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()

with sqlite3.connect('database.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS users(
        login TEXT, 
        password TEXT,
        name TEXT,
        email TEXT,
        admin TEXT

)
    """
    db.executescript(table)

class CardItem(MDCard):
    pass

LabelBase.register(name='text',
                      fn_regular='/TravelGo-V2/Style/ba.ttf')
LabelBase.register(name='text_double',
                      fn_regular='/TravelGo-V2/Style/Mikar.ttf')
class TravelGO(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.material_style = "M3"
        return Builder.load_file("kivy.kv")

    def search_news(self):
        a = self.root.ids
        TEXT = f'{a.search_field2.text}, кафе'
        # колличество запросов, то есть заведений которых код выдаст, максимум 50
        RESULTS = 10

        response = requests.get(
            f'https://search-maps.yandex.ru/v1/?apikey={API}&text={TEXT}&lang=ru_RU&results={RESULTS}')
        text = json.loads(response.text)
        print(len(text['features']))
        for i in text['features']:
            # тут по порядку: название, вид, описание, адресс, номер, время работы. Делай с ними что хочешь в этом цикле
            name = i['properties']['CompanyMetaData']['name']
            clas = i['properties']['CompanyMetaData']['Categories'][0]['name']
            description = i['properties']['description']
            address = i['properties']['CompanyMetaData']['address']
            phone = i['properties']['CompanyMetaData']['Phones'][0]['formatted']
            hours = i['properties']['CompanyMetaData']['Hours']['Availabilities']
            # print(name, '\n', clas, '\n', description, '\n', address, '\n', hours, '\n')
            content = CardItem()
            content.ids.title.text = f"{name}"
            content.ids.dect.text = f"{clas}"
            print(content.ids.title.text)

            a.rv2.add_widget(content)
    def registration(self, a=True):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        email = self.root.ids.email.text
        name = self.root.ids.name.text
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])

            if cursor.fetchone() is None:
                if a == True:
                    values = [login, password, email, name, a]
                    cursor.execute("INSERT INTO users(login, password, email, name, admin) VALUES(?,md5(?),?,?,?)", values)
                    toast("Создали акаунт")
                    self.screen('useradmin')
                    db.commit()
                elif a == False:
                    values = [login, password, email, name, a]
                    cursor.execute("INSERT INTO users(login, password, email, name, admin) VALUES(?,md5(?),?,?,?)",values)
                    toast("Создали акаунт")
                    self.screen('user')
                    db.commit()

            else:
                toast("Tакой логин уже есть")

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()

    def log_in(self):
        login = self.root.ids.login.text
        password = self.root.ids.password.text
        try:
            db = sqlite3.connect("database.db")
            cur = db.cursor()
            db.create_function("md5", 1, md5sum)
            cur.execute("SELECT login FROM users WHERE login = ?", [login])
            if cur.fetchone() is None:
                toast("Такого логина не существует")
            else:
                cur.execute("SELECT login FROM users WHERE login = ? AND password = md5(?)", [login, password])
                if cur.fetchone() is None:
                    toast("Пороль не верный")
                else:
                    cur.execute(f'''SELECT * FROM users WHERE login LIKE '%{login}%';''')
                    three_results = cur.fetchall()
                    print(three_results[0][4])
                    if three_results[0][4] == "1":
                        toast("Привет, партнер")
                        self.screen("admin")
                    else:
                        toast("Вы вошли")
                        self.screen("user")
        finally:

            cur.close()
            db.close()

    def screen(self, screen_name):
        self.root.current = screen_name

    def data(self, m):
        if m == 1:
            anim = Animation(pos_hint=({"center_x": .51, "center_y": .51}))
            anim.start(self.root.ids.singuser)
        elif m == 2:
            anim = Animation(pos_hint=({"center_x": .522, "center_y": .522}))
            anim.start(self.root.ids.singadmin)


TravelGO().run()