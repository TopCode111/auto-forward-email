
import webbrowser 
# Documnetation of webbrowser module - https://docs.python.org/3/library/webbrowser.html
import sys

args = sys.argv[1:]   # By default sys.argv[0] is the name of the script. So we start looking for the arguments starting from index 1

if args:

	tab_specify = 2  #Open a new browser tab
	url = sys.argv[1]
	webbrowser.open(url, new=tab_specify)

else:
	print("Please provide a valid URL to open")