from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.metrics import dp, sp
from kivy.utils import get_color_from_hex

PRIMARY = get_color_from_hex('#2E7D32')
ERROR = get_color_from_hex('#C62828')
WARNING = get_color_from_hex('#F9A825')


class Toast:
    """Sistema de notificaciones toast reutilizable."""

    @staticmethod
    def show(parent, mensaje, duracion=2.0, color=None):
        if color is None:
            color = PRIMARY

        toast = Label(
            text=mensaje,
            font_size=sp(16),
            color=(1, 1, 1, 1),
            size_hint=(0.8, None),
            height=dp(50),
            halign="center",
            valign="middle",
        )

        popup = Popup(
            content=toast,
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={"center_x": 0.5, "y": 0.05},
            background_color=(0, 0, 0, 0),
            auto_dismiss=False,
            separator_height=0,
        )

        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), duracion)
