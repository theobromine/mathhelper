from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from sympy import *


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
            a = solve((a*(x**2))+(b*x)+c, x)
            x1 = a[0]
            x2 = a[1]
            self.result.text = pretty(x1) + '\n' + pretty(x2)
        else:
            self.result.text = 'D negative'


class SystemsOfEquations(Screen):
    def math(self, instance):
        x = Symbol('x')
        y = Symbol('y')
        eq1 = sympify(self.fa.text)
        sol1 = sympify(self.fb.text)
        eq2 = sympify(self.sa.text)
        sol2 = sympify(self.sb.text)
        a = solve([Eq(eq1, sol1), Eq(eq2, sol2)], [x, y])
        self.sr.text = pretty(a)


class MathFunction3(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


main_screen = Builder.load_string('''
MyScreenManager:
    MainScreen:
    SquareEquals:
    SystemsOfEquations:
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
            text: 'Systems of equations'
            size_hint: (.5, .5)
            on_release: app.root.current = 'SystemsOfEquations'
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
<SystemsOfEquations>:
    name: 'SystemsOfEquations'
    fa: _fa
    fb: _fb
    sa: _sa
    sb: _sb
    sr: _sr
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1,1)
        Label:
            text: 'Systems of equations (use only "x" and "y"!)'
            font_size: 25
            size_hint: (.2,.1)
        GridLayout:
            cols: 3
            TextInput:
                id: _fa
                multiline: False
            Label:
                text: '='
            TextInput:
                id: _fb
                multiline: False
            TextInput:
                id: _sa
                multiline: False
            Label:
                text: '='
            TextInput:
                id: _sb
                multiline: False
            Button:
                text: 'Do the math'
                on_release: root.math(*args)
            Label:
                id: _sr
                text: ''
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
