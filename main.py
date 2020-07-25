import os
import re
import time
import pafy
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


def get_inserted_links():
    #https://www.youtube.com/watch?v=PWt27h_scaYhttps://www.youtube.com/watch?v=bgtS7qoRnjEhttps://www.youtube.com/watch?v=9arsAqNZ8tU

    protocol_string = "https://"
    url_list = None
    error = False

    try:
        url_list = url_field.get("1.0", "end-1c").split(protocol_string)
        url_list.pop(0)
    except Exception:
        error = True
    finally:
        if error:
            print("Error")
        else:
            for url in url_list:
                print("https://" + url)


print("Kek")
main_window = Tk()

main_window.title("YouTube => MP3 Downloader")
main_window.config(bg='#3498DB')
main_window.geometry("500x400")

# Label
label = Label(main_window, text="Insert your links to field below")
label.pack()

# URL text field
url_field = Text(main_window, height=14, width=60)
url_field.pack()

# Download button
download_button = Button(main_window, text="Download", font=(
    "Times New Roman", 14), relief='ridge', activeforeground='red', command=get_inserted_links)
download_button.pack(side=TOP)

main_window.mainloop()




