#Author: Justin Clark
#Google from the command line with this small python script.

import webbrowser
import random
import time

#int wait_time # Waits for wait_time [Seconds]

while (1):
    text_file = open("PatrioticTerms.txt", "r")
    lines = text_file.readlines()
    line_length = len(lines);
    search_term = lines[random.randint(3,len(lines)-1)]
    #search_term = lines[1]; #test first line of search
    text_file.close()
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search_term)
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
 
