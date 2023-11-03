
import json
import hashlib
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivymd.app import MDApp
from kivy.lang.builder import Builder
import requests
import sqlite3
from kivy.core.text import LabelBase
from kivymd.toast import toast
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
class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
LabelBase.register(name='text',
                      fn_regular='Style/ba.ttf')
LabelBase.register(name='text_double',
                      fn_regular='Style/Mikar.ttf')
class TravelGO(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.material_style = "M3"
        return Builder.load_file("kivy.kv")
    def search_news(self):
        self.root.ids.rv2.clear_widgets()
        TEXT = f'{self.root.ids.search_field2.text}, кафе'
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
            self.root.ids.rv2.add_widget(
                MD3Card
                (
                    MDBoxLayout(
                        MDLabel(
                            id="title",
                            text=f"{name}",
                            font_style="H5",
                            bold=True,
                            adaptive_height=True,
                        ),
                        MDLabel(
                            id="title",
                            text=f"{clas}",
                            bold=True,
                            adaptive_height=True,
                        ),
                        MDLabel(
                            id="title",
                            text=f"{description}",
                            bold=True,
                            adaptive_height=True,
                        ),
                        orientation="vertical",
                        adaptive_height=True,
                        spacing="6dp",
                        padding="12dp",
                        pos_hint=({"center_y": .5}),
                    ),


                        # MDLabel
                        # id: dect
                        # text: "Subtitle text"
                        # theme_text_color: "Hint"
                        # adaptive_height: True
                    size_hint_y=None,
                    height="86dp",
                    padding="4dp",
                    radius=12,


                )



            )

            print("Ok")
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