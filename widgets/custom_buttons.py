from kivy.uix.button import Button
from kivy.properties import ListProperty

class RoundedButton(Button):
    radius = ListProperty([10])  # Radio de las esquinas
    fill_color = ListProperty([0, 0, 0, 0.25])  # Color actual del botón

class LoginButton(Button):
    fill_color = ListProperty([0, 1, 0, 0.7])  # Color actual del botón
