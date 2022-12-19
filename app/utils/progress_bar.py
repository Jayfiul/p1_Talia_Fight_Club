import math
import sys
import time

characters = ["▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]

class ProgressBar:
    def __init__(self, total, width=50):
        self.total = total
        self.width = width
        self.current = 0
        self.progress = 0
        self.start_time = time.time()

    def update(self, new_progress, message=""):
        self.current = new_progress
        self.progress = self.current / self.total
        self.draw(message)

    def draw(self, message=""):
        bar = "█" * int(self.progress * self.width)
        bar += characters[int((self.progress * self.width - len(bar)) * 8)]
        bar += " " * (self.width - len(bar))
        time_elapsed = time.time() - self.start_time
        time_left = None
        # First clear the line completely by filling it with spaces
        sys.stdout.write(" " * (self.width + 50))
        # Then move the cursor back to the beginning of the line
        sys.stdout.write("\r")
        try:
            time_left = time_elapsed / self.progress - time_elapsed
        except ZeroDivisionError:
            time_left = None
        text = "\rProgress: |{}| {:.1f}% - {} - ETA: {}s".format(
            bar, math.floor(self.progress * 1000) / 10, message, ("N/A" if time_left is None else math.floor(time_left * 10) / 10)
        )
        sys.stdout.write(text)
        sys.stdout.flush()

    def finish(self, message=""):
        self.update(self.total, message)
        print()
