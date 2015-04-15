from kivy.app import App
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
        # equals = [self.fe.text, self.se.text]
        # question = []
        # answers = [self.fa.text, self.sa.text]
        # tmp = ''
        # smbs = []
        # for i in range(len(equals)-1):
            # for j in range(len(str(equals[i]))-1):
                # if str(equals[i])[j].isalpha():
                    # smbs.append(str(equals[i])[j])
            # for k in range(len(answers)-1):
                # for l in range(len(str(answers[i]))-1):
                    # str(answers[i])[k].replace('+', '-')
                    # str(answers[i])[k].replace('-', '+')
            # tmp = str(equals[i])+','+str(answers[k])
            # question.append(sympify(tmp))
        x = Symbol('x')
        y = Symbol('y')
        eq1 = sympify(self.fe.text)
        sol1 = sympify(self.fa.text)
        eq2 = sympify(self.se.text)
        sol2 = sympify(self.sa.text)
        a = solve([Eq(eq1, sol1), Eq(eq2, sol2)], [x, y])
        self.l1.text = pretty(a)


class MathFunction3(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    MyApp().run()
