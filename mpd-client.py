from mpd import MPDClient
import time

client = MPDClient()
client.connect("192.168.1.134", 6600)

# client.pause()
# client.next()
# client.previous()
# client.stop()
# client.setvol(70)

while True:
	current_song = client.currentsong()
	status = client.status()

	print(status)

	print(f"Artist: {current_song['artist']}\nTitle: {current_song['title']}\nAlbum: {current_song['album']}")
	print(f"time: {status['time']} elapsed: {status['elapsed']}")
	print("====================================================================")
	time.sleep(1)
