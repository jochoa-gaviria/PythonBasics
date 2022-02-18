from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os, json
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "signUp_screen"

class SignUpScreen(Screen):
    def addUser(self, username, password):
        if os.path.exists('users.json'):
            with open('users.json') as file:
                users = json.load(file)
            users[username] = {"username": username, "password": password,
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            
            with open('users.json', 'w') as file:
                json.dump(users, file)
            self.manager.current = 'SignUpSucess_screen'

class SignUpSucessScreen(Screen):
    def loginPage(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()