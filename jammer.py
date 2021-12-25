"""
THIS IS IN VERY VERY VERYYYY Early development PLEASE report issues to me asap
"""
# import modules
import os
import random
import playsound
from plyer import notification

# This is my path
path = input("what path is the music in?")

# to store files in a file_names

file_names = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if ".mp3" in f:
            file_names.append(f)

while True:
    songtoplay = random.choice(file_names)
    title = "Jammer"

    message = "Now playing: " + songtoplay + "\n" + "Enjoy!"

    notification.notify(
        title=title, message=message, app_icon="", timeout=10, toast=False
    )
    try:
        playsound.playsound("/home/lubu/Music/" + str(songtoplay))
    except KeyboardInterrupt:
        break
