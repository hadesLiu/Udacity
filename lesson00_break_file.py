import webbrowser

import time

total_breaks = 3
break_count = 0
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://music.163.com/#/mv?id=5500070")
    break_count += 1
