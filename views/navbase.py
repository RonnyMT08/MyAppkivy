from kivy.uix.screenmanager import Screen

class NavBaseView(Screen):
    def cambiar_color_nav(self, btn, lb):
        btn.canvas.before.children[0].rgba = (1, 1, 1, 1)
        lb.font_name = "assets/fonts/RobotoSlab-Bold"
        lb.color = (1, 1, 1, 1)
