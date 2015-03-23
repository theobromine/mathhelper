from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from math import sqrt


class MainScreen(Screen):
    pass
    # def __init__(self, **kwargs):
    #     super(MainScreen, self).__init__(**kwargs)
    #
    #     layout = FloatLayout(size=(300, 300))
    #     button1 = Button(text="Do math function", size_hint=(.5, .5), pos_hint={"left": 2, 'top': 2})
    #     button1.bind(on_press=self.sqeq)
    #     layout.add_widget(button1)
    #
    #
    # def sqeq(self, *args):
    #     self.manager.current = 'SquareEquals'
    # # coming soon:
    # # def slau(self, *args):
    #     # self.manager.current = 'SLAU'
    #
    # # def pifa(self, *args):
    #     # self.manager.current = 'Pifagor'
    #
    # # def geron(self, *args):
    #     # self.manager.current = 'Geron'


class SquareEquals(Screen):
    pass
    # def count(self, a, b, c):
    #     a = int(a)
    #     b = int(b)
    #     c = int(c)
    #     global D, x1, x2
    #     D = 0
    #     x1 = 0
    #     x2 = 0
    #     D = b**2-4*a*c
    #     if D >= 0:
    #         x1 = ((-1 * b) + sqrt(D))/(2*a)
    #         x2 = ((-1 * b) - sqrt(D))/(2*a)
    #
    #         ti4.text = x1
    #         ti5.text = x2
    #         ti6.text = D
    #         return x1, x2, D
    #     else:
    #         print("negative")
    #         return 0
    #
    # def __init__(self, **kwargs):
    #     super(SquareEquals, self).__init__(**kwargs)
    #
    #     layout = FloatLayout(size=(100, 100))
    #     ti = TextInput(multiline=False, text='1', size_hint=(.2, .2), pos_hint={"left": 1, 'top': 1})
    #     ti2 = TextInput(multiline=False, text='1', size_hint=(.2, .2), pos_hint={"left": 3, 'top': 1})
    #     ti3 = TextInput(multiline=False, text='1', size_hint=(.2, .2), pos_hint={"left": 5, 'top': 1})
    #     layout.add_widget(ti)
    #     layout.add_widget(ti2)
    #     layout.add_widget(ti3)
    #     b1 = Button(text='solve!', size_hint=(1, .2), pos_hint={"left": 1, 'top': 2})
    #     b1.bind(on_press=self.count(ti.text, ti2.text, ti3.text))
    #     global ti4, ti5, ti6
    #     ti4 = TextInput(multiline=False, size_hint=(.2, .2), pos_hint={"left": 2, 'top': 3})
    #     ti5 = TextInput(multiline=False, size_hint=(.2, .2), pos_hint={"left": 2, 'top': 4})
    #     ti6 = TextInput(multiline=False, size_hint=(.2, .2), pos_hint={"left": 2, 'top': 5})
    #     l1 = Label(text='x[sup]2[/sup] + ', size_hint=(.125, .2), pos_hint={"left": 2, 'top': 1})
    #     l2 = Label(text='x + ', size_hint=(.125, .2), pos_hint={"left": 4, 'top': 1})
    #     l3 = Label(text='= 0', size_hint=(.15, .2), pos_hint={"left": 6, 'top': 1})
    #     l4 = Label(text='x1 = ', size_hint=(.2, .2), pos_hint={"left": 1, 'top': 1})
    #     l5 = Label(text='x2 = ')
    #     l6 = Label(text='D = ')
    #     bex = Button(text='win?')
    #     bex.bind(on_press=self.menu)
    #     layout.add_widget(ti4)
    #     layout.add_widget(ti5)
    #     layout.add_widget(ti6)
    #     layout.add_widget(b1)
    #     layout.add_widget(bex)
    #     layout.add_widget(l1)
    #     layout.add_widget(l2)
    #     layout.add_widget(l3)
    #     layout.add_widget(l4)
    #     layout.add_widget(l5)
    #     layout.add_widget(l6)
    #
    # def menu(self, *args):
    #     self.manager.current = 'Main'
import time
import random

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass
main_screen = Builder.load_string('''
MyScreenManager:
    MainScreen:
    SquareEquals:
<MainScreen>:
    name: 'MainScreen'
    FloatLayout:
        size: (300,300)
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 30
                on_release: app.root.current = 'SquareEquals'
<SquareEquals>:
    name: 'SquareEquals'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Square Equals'
            font_size: 30
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'MainScreen'

<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
''')

class MyApp(App):

    def build(self):
        return main_screen

if __name__ == '__main__':
    MyApp().run()