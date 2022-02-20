import glob
import random
import os, json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
from pathlib import Path

from matplotlib.style import available

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "signUp_screen"


    def Login(self, username, pwd):
        if os.path.exists('users.json'):
            with open('users.json') as file:
                users = json.load(file)
            if username in users and users[username]['password']==pwd:
                self.manager.current = 'loginSuccess_screen'
            else: 
                self.ids.message.text = "Wrong username or password!!"
                

class SignUpScreen(Screen):
    def addUser(self, username, password):
        if username != '' and password != '':
            if os.path.exists('users.json'):
                with open('users.json') as file:
                    users = json.load(file)
                users[username] = {"username": username, "password": password,
                "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                
                with open('users.json', 'w') as file:
                    json.dump(users, file)
                self.manager.current = 'SignUpSuccess_screen'
        else: 
            self.ids.messageData.text = "Pls complete all data information"

    def backLogin(self):
        self.manager.current = 'login_screen'

class SignUpSuccessScreen(Screen):
    def loginPage(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'


class LoginSuccessScreen(Screen):
    def logOut(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
    
    def enlighten(self, feeling):
        feeling = feeling.lower()
        if os.path.exists('quotes'):
            availableFeeling = glob.glob('quotes/*txt')
            availableFeeling = [Path(filename).stem for filename in availableFeeling]

            if feeling in availableFeeling:
                with open(f'quotes/{feeling}.txt') as file:
                    enlight = list(file)
                self.ids.enlighten.text = random.choice(enlight)
            else:
                self.ids.enlighten.text = "Try another feeling"
        else:
            self.ids.enlighten.text = "There's no feeling into the database"


class ImageButton(HoverBehavior, Image, ButtonBehavior):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()