from services import Client
import time

mpd_client = Client("192.168.1.134")

mpd_client.play()

while True:
    mpd_client.get_song_info()
    time.sleep(1)