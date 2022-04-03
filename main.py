from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('screen_one.kv')
Builder.load_file('screen_two.kv')
Builder.load_file('screen_three.kv')

class MyPopup(Popup):
    pass


class pages1(Screen):
    def open_popup(self):
        return MyPopup().open()


class Screen_One(Screen):
    pass


class Screen_Two(Screen):
    pass


class Screen_Three(Screen):
    pass

# main class app
class main_page(App):
    icon = "img/logo-icon.png"
    title = 'control panel'

    def build(self):
        mng = ScreenManager(transition=NoTransition())
        mng.add_widget(pages1(name='home'))
        mng.add_widget(Screen_One(name='one'))
        mng.add_widget(Screen_Two(name='two'))
        mng.add_widget(Screen_Three(name='three'))
        return mng


if __name__ == '__main__':
    main_page().run()
