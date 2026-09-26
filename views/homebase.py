from kivy.uix.screenmanager import Screen

class HomeBaseView(Screen):
    def cambiar_color_nav(self, btn, lb):
        btn.canvas.before.children[0].rgba = (1, 1, 1, 1)
        lb.font_name = "assets/fonts/RobotoSlab-Bold"
        lb.color = (1, 1, 1, 1)
    def reset_color_nave(self, btn, lb):
        btn.canvas.before.children[0].rgba = (1, 1, 1, 0.5)
        lb.font_name = "assets/fonts/RobotoSlab-Regular"
        lb.color = (1, 1, 1, 0.5)
    def go_home(self):
        self.manager.current = 'home'
    def go_reservas(self):
        self.manager.current = 'reservas'
    def go_contacto(self):
        self.manager.current = 'contacto'
    def go_cuenta(self):
        self.manager.current = 'cuenta'
    def go_login(self):
        self.manager.current = 'login'
