import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_cont < total_breaks):
	time.sleep(10)
	webbrowser.open("http://youtube.com")
	break_count = break_count + 1

