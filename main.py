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
import time
Window.size = (480, 800)
API = '6c39b074-59ea-4ce3-8924-c1b26f5e9137'

class CardItem(MDCard):
    pass

class TravelGO(MDApp):
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

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("kivy.kv")

TravelGO().run()