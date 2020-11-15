from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.popup import Popup

Window.size = (360,630)

user_password = {"Julian":12345678}
class Principal(Screen):
    pass
class consumidor(Screen):
    pass

class registro(Screen):
    pass
class P(Screen):
    pass
class R(Screen):
    pass

class emprendedor(Screen):
    def anim(self,widget):
        anim = Animation(pos_hint={"center_y":1.16})
        anim.start(widget)
    def anim1(self,widget):
        anim = Animation(pos_hint={"center_y":.85})
        anim.start(widget)
    def icons(self,widget):
        anim = Animation(pos_hint={"center_y":.8})
        anim += Animation(pos_hint={"center_y":.85})
        anim.start(widget)
    def text(self,widget):
        anim = Animation(opacity=0,duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)

sm = ScreenManager()
sm.add_widget(Principal(name='p'))
sm.add_widget(consumidor(name='c'))
sm.add_widget(emprendedor(name='e'))

class DemoApp(MDApp):
    data = {
        'food': 'Gastronomía',
        'glass-cocktail': 'Entretenimiento',
        'recycle': 'Propuestas Ecológicas',
    }
    def show_popup(self):
        show = P()
        popupWindow = Popup(title="  Usuario y/o Contraseña Incorrectos", content=show, size_hint=(None,None),size=(300,130))
        popupWindow.open()
    def show_register(self):
        show = R()
        popupWindow = Popup(title="   Campos Inválidos!!!", content=show, size_hint=(None,None),size=(350,130))
        popupWindow.open()
    def validarSesion(self,instance,instance2):
        user = instance2.text
        ps = instance.text
        if user_password.get(user,"") == ps:
            return True
        else:
            self.show_popup()
    def validarReg(self,name,pwd,mail,info,spinner):
        user = name.text
        ps = pwd.text
        mail = mail.text
        inf = info.text
        opt = spinner.text
        if ps!="" and user!="" and mail!="" and inf!="" and opt!="Tipo de Emprendimiento" and user not in user_password and len(ps)>=8:
            dic_temporal = {user:ps}
            user_password.update(dic_temporal)
            print(user_password)
            return True
        else:
            self.show_register()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange" 
        screen = Builder.load_file("style.kv")
        return screen




DemoApp().run()

