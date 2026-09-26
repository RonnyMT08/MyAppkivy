# Pantalla de kivy /views/login.py   
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class LoginView(Screen):
    def cambiar_color_nav(self, btn, lb):
        btn.canvas.before.children[0].rgba = (1, 1, 1, 1)
        lb.font_name = "assets/fonts/RobotoSlab-Bold"
        lb.color = (1, 1, 1, 1)
    
    email_ingresado = ObjectProperty(None)
    contrasenia_ingresada = ObjectProperty(None)

    def capturar_login(self, email, contrasenia):
        if email == "admin@gmail.com" and contrasenia == "1234":
            self.manager.current = "homebase"
        else:
            popup = Popup(
                title="Error",
                content=Label(text="Email o contraseña incorrectos"),
                size_hint=(0.6, 0.3)
            )
            popup.open()

    def go_home(self):
        self.manager.current = "homebase"
        