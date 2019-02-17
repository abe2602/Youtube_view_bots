import webbrowser 
import time 
import os 

inpt = "" #Put the video URL between the commas
inpt2 = 30 #Time to create another instance of the video
inpt3 = "Firefox" #Browser

def OpenUrl(): 
	i = 0

	while(i < 300):
		print ("Viewed.") 
		webbrowser.open(inpt) #Open new browser with the video
		time.sleep(int(inpt2)) 
		
		if(i%50 == 0):
			os.system("TASKKILL /F /IM " + inpt3 + ".exe") #kill the task

		i += 1

OpenUrl()