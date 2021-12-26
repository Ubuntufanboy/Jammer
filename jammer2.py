"""
This is the Improved Command line music player!
This is still in development. This is an improvement of the jammer.py
"""

#these should work because these come with python
try:
    import os
    import random
except ImportError:
    print("Error: import error PLEASE REPORT THIS TO THE DEVELOPER")


#these may not work because they are not in python
try:
    import playsound
except:
    print("Please install playsound")


try:
    from plyer import notification
except:
    print("Please install plyer")

print("This is in early development. Please report any bugs to the developer")

print("One last thing... If a song that you don't want to listen to is in the next song, \nplease press ctrl+c. It will stop the program right before that song will play.")
path = input("Enter the path of the music folder: ")

file_names = []

for (root, dirs, file) in os.walk(path):
	for f in file:
		if '.mp3' in f:
			file_names.append(f)

order = []

for i in range(len(file_names)*10):
    order.append(random.choice(file_names))

count = 0    
while True:
    songtoplay = order[count]
    
    title = 'Jammer'

    message = 'Now playing: ' + songtoplay + '\n' + 'Enjoy!'
    
    messagee = 'NEXT playing: ' + order[count + 1]
    
    notification.notify(title= title,
                        message= message,
                        app_icon = "/home/lubu/Downloads/lorder.png",
                        timeout= 10,
                        toast=False)
    
    notification.notify(title= title,
                        message= messagee,
                        app_icon = "/home/lubu/Downloads/lorder.png",
                        timeout= 10,
                        toast=False)
    
    try:
        playsound.playsound("/home/lubu/Music/" + str(songtoplay))
        count += 1
    except KeyboardInterrupt:
        break
