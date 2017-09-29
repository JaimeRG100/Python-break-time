# Plays a Youtube video in a browser 3 times each 10 seconds

import time
import webbrowser

total_breaks = 3
total_count = 0
print("This programa started on " + time.ctime())
while total_count < total_breaks :
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    total_count = total_count + 1
