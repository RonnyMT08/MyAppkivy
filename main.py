from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager

from screens.homebase import HomeBase
from screens.login.loginbase import LoginBase
from screens.navbase import NavBase

from screens.home import Home
from screens.contacto import Contacto
from screens.reservas import Reservas
from screens.cuenta import Cuenta


class MyApp(App):
    def build(self):
        self.title = "My Kivy App"
        self.icon = "assets/images/icon.png"

        Builder.load_file("screens/login/loginbase.kv")
        Builder.load_file("screens/login/login.kv")
        Builder.load_file("screens/login/newuser.kv")
        Builder.load_file("screens/login/password.kv")
        
        Builder.load_file("screens/homebase.kv")

        Builder.load_file("screens/navbase.kv")

        Builder.load_file("screens/mapas.kv")
        Builder.load_file("screens/kits.kv")
        Builder.load_file("screens/modos.kv")
        Builder.load_file("screens/publica.kv")
        Builder.load_file("screens/privada.kv")

        Builder.load_file("screens/cuenta.kv")
        Builder.load_file("screens/contacto.kv")
        Builder.load_file("screens/reservas.kv")
        Builder.load_file("screens/home.kv")

        sm = ScreenManager()
        sm.add_widget(LoginBase(name="loginbase"))
        sm.add_widget(NavBase(name="navbase"))
        sm.add_widget(HomeBase(name="homebase"))
        sm.add_widget(Home(name="home"))
        sm.add_widget(Contacto(name="contacto"))
        sm.add_widget(Reservas(name="reservas"))
        sm.add_widget(Cuenta(name="cuenta"))
        return sm

if __name__ == "__main__":
    MyApp().run()
