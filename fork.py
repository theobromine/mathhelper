from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from sympy import *
from math import sqrt


class MainScreen(Screen):
    pass


class SquareEquals(Screen):
    def math(self, instance):
        a = int(self.a.text)
        b = int(self.b.text)
        c = int(self.c.text)
        x = Symbol('x')
        dis = int(self.b.text)**2 - 4 * int(self.a.text) * int(self.c.text)
        if dis >= 0:
            ans = solve((a*(x**2))+(b*x)+c, x)
            x1 = ans[0]
            x2 = ans[1]
            self.result.text = 'x1 = '+str(x1)+'\n x2 = '+str(x2)+'\n D = '+str(dis)
        else:
            self.result.text = 'D negative'

class MathFunction2(Screen):
    pass


class MathFunction3(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


main_screen = Builder.load_string('''
MyScreenManager:
    MainScreen:
    SquareEquals:
    MathFunction2:
    MathFunction3:
<MainScreen>:
    name: 'MainScreen'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Square equals'
            size_hint: (.5, .5)
            on_release: app.root.current = 'SquareEquals'
        Button:
            text: 'Math function # 2'
            size_hint: (.5, .5)
            on_release: app.root.current = 'MathFunction2'
        Button:
            text: 'Math function # 3'
            size_hint: (.5, .5)
            on_release: app.root.current = 'MathFunction3'
<SquareEquals>:
    a: _a
    b: _b
    c: _c
    result: _result
    name: 'SquareEquals'
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1,1)
        Label:
            text: 'Square Equals'
            font_size: 30
            size_hint: (.3,.1)
        GridLayout:
            rows: 2
            orientation: 'vertical'
            TextInput:
                id: _a
                multiline: 'false'
            TextInput:
                id: _b
                multiline: 'false'
            TextInput:
                id: _c
                multiline: 'false'
            Button:
                text: 'Do the math'
                on_release: root.math(*args)
            Button:
                id: _result
                text: ''
            BoxLayout:
                Button:
                    text: 'Go to main screen'
                    font_size: 30
                    on_release: app.root.current = 'MainScreen'
<MathFunction2>:
    name: 'MathFunction2'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Math Function 2'
            font_size: 30
        BoxLayout:
            Button:
                text: 'Go to main screen'
                font_size: 30
                on_release: app.root.current = 'MainScreen'
<MathFunction3>:
    name: 'MathFunction3'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Math Function 3'
            font_size: 30
        BoxLayout:
            Button:
                text: 'Go to main screen'
                font_size: 30
                on_release: app.root.current = 'MainScreen'
''')


class MyApp(App):
    def build(self):
        return main_screen


if __name__ == '__main__':
    MyApp().run()
