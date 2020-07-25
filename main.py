import os
import re
import time
import pafy
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

# TODO add info from terminal to tkinter, add path to save, block (?) and clear textfield


def check_youtube_link(link):
    pattern = re.compile("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")
    return pattern.match(link)


def download_video(download_url):
    start_time = time.time()

    # noinspection PyBroadException
    try:
        video = pafy.new(download_url)
        print(f"'{video.title}'. Length: {video.duration}.")
        print("Downloading started")

        best_audio = video.getbestaudio()
        best_audio.download(filepath=f"/{os.getcwd()}/{video.title}.mp3")

        print("--- %s seconds ---" % (time.time() - start_time))
        print(f"'{video.title}' downloaded")
    except Exception:
        print("Error occurred.")


def get_inserted_links():
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
                url = "https://" + url
                link_match = check_youtube_link(url)
                if link_match is not None:
                    print(url, "OK")
                    download_video(url)
                else:
                    print(url, "Incorrect link!")


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




