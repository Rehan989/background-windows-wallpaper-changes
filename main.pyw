import ctypes
from tkinter import *
import winreg as reg
import os
import json
import dotenv
import requests
import datetime
import time

dotenv.load_dotenv()

os.chdir('G:/New folder/TTS/wallpaperChanging')

json_file = open('conf.json')
conf = json.load(json_file)

class Main:
    path = str(os.getcwd())

    def download_image(self):
        Headers = { "Authorization" : f"Client-ID {os.environ.get('ACCESS_KEY')}" }
        request = requests.get("https://api.unsplash.com/photos/random?per_page=1&query=wallpaper?order_by=latest?orientation=landscape",headers=Headers)
        request = requests.get(request.json()["urls"]["full"],headers=Headers)
        filename = 'image.jpg'
        if(request.status_code==200):
            with open(filename, 'wb') as f:
                f.write(request.content)
            json_file = open("conf.json")
            conf = json.load(json_file)
            json_file = open("conf.json", "w")
            json_file.writelines(json.dumps({
                **conf,
                'last_image_update_time':str(datetime.datetime.now().replace(microsecond=0)),
                'next_image_update_time':str(datetime.datetime.now().replace(microsecond=0)+datetime.timedelta(minutes = int(conf['background_change_time_in_minutes'])))
            }))
    def run_background(self):
        while(True):
            json_file = open('conf.json')
            conf = json.load(json_file)
            if(str(datetime.datetime.now().replace(microsecond=0))==conf["next_image_update_time"]):
                self.download_image()
                self.set_wallpaper("image.jpg")
                print("yes")
            print("no")
            print(str(datetime.datetime.now().replace(microsecond=0))==conf["next_image_update_time"])
            print(str(datetime.datetime.now().replace(microsecond=0)))
            print(conf["next_image_update_time"])
            time.sleep(3)

    def set_wallpaper(self, image_name):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{self.path}\\{image_name}" , 0)

application = Main()

if (conf["run_in_background"]):
    application.download_image()
    application.set_wallpaper("image.jpg")
    application.run_background()
else:
    application.download_image()
    application.set_wallpaper("image.jpg")


