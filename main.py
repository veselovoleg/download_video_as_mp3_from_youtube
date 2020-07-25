import os
import re
import time
import pafy


def main():
    print("Insert link to YouTube video")
    url = input()
    link_match = check_youtube_link(url)

    if link_match is not None:
        download_video(url)
    else:
        print("Incorrect link!")


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


def check_youtube_link(link):
    pattern = re.compile("^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")
    return pattern.match(link)


if __name__ == "__main__":
    # execute only if run as a script
    main()
