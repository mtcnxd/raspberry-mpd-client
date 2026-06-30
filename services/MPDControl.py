class Client:
    def __init__(self, host: str):
        self.client = MPDClient()
        self.client.connect(host, 6600)

    def get_playlist(self):
        return self.client.playlistinfo()

    def play(self):
        self.client.play()

    def get_song_info(self):
        return self.client.currentsong()

    def get_time_info(self):
        status = self.get_status()

        elapsed = float(status["elapsed"])
        duration = float(status["duration"])

        elapsed_minutes = int(elapsed // 60)
        elapsed_seconds = int(elapsed % 60)

        return {f"elapsed: {elapsed_minutes:02} duration: {duration_minutes:02}"}

    def get_progress(self):
        status = self.get_time_info()

    def get_progress_bar(self):
        length = 20
        filled = int(progress / 100 * length)
        bar = "█" * filled + "░" * (length - filled)
        print(f"[{bar}] {progress:.0f}%")

    def get_status(self):
        return self.client.status()    