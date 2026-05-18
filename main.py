from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

Window.clearcolor = (0.08, 0.10, 0.14, 1)

class LoginScreen(Screen):
    def login_app(self, username, password):
        if username.strip() and password.strip():
            self.manager.current = "home"
        else:
            print("Por favor ingresa usuario y contraseña")

    def create_user(self):
        self.manager.current = "settings"

    def exit_app(self):
        App.get_running_app().stop()

class HomeScreen(Screen):
    def go_settings(self):
        self.manager.current = "settings"

class SettingsScreen(Screen):
    def go_home(self):
        self.manager.current = "home"

class RoundedButton(Button):
    fill_color = ListProperty([0, 0, 0, 0.25])
    radius = ListProperty([20, 20, 20, 20])

class LoginButton(Button):
    fill_color = ListProperty([0, 1, 0, 0.8])
    radius = ListProperty([10, 10, 10, 10])

class MyApp(App):
    def build(self):
        self.title = "My Kivy App"
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    MyApp().run()
