from kivy.uix.screenmanager import Screen
from widgets.toast import Toast
from widgets import ERROR

class LoginView(Screen):
    def capturar_login(self, email, contrasenia):
        if email == "admin@gmail.com" and contrasenia == "1234":
            Toast.show(self, "Login correcto")
            self.manager.current = "homebase"
        else:
            Toast.show(self, "Credenciales invalidas", color=ERROR)
