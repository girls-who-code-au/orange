#INSTALL pygame library as administrator:
#from python\scripts folder> pip install pygame
#from python\scripts folder> pip show pygame

##setup pygame
import sys, pygame
pygame.init()
size = width, height = 640, 480
##screen = pygame.display.set_mode(size)

##setup filepaths --- use escape slashes (double up)
from pathlib import Path
#the concatenated string below is specific to my folder structure; adjust to your own:
userbasepath = str(Path.home())+"\\orange\\"

### MEDIA SECTION ##############################################################
###home pic
##homepicfilepath = userbasepath + "home.jpg"
##homepicBIG = pygame.image.load(homepicfilepath)
##homepic = pygame.transform.scale(homepicBIG, (640,480))
##
###school pic
##schoolpicfilepath = userbasepath + "terracycleposterweb.jpg"
##schoolpicBIG = pygame.image.load(schoolpicfilepath)
##schoolpic = pygame.transform.scale(schoolpicBIG, (640,480))
##
###music box sound; exit sound so need a time delay
import time
##musicboxfilepath = userbasepath + "Music_Box-Big_Daddy-1389738694.wav"
##pygame.mixer.music.load(musicboxfilepath)

################################################################################

#top level function
def startGame():
  state = "start"
  while state != "resolved":
    pygame.event.get()
    printOptions(state)  
    choice = input("What to do? : ")    
    state = changeState(state,choice)
  time.sleep(3)
  pygame.quit()
  
#print options for each location
def printOptions(state):
  if state == "start":
##    pygame.draw.rect(screen,(0,0,0),(0,0,640,480))
##    screen.blit(homepic, (0,0))
##    pygame.display.flip()
    print("You're in the line for lunch at school when you see another kid get ")
    print("pushed by a bigger kid; the smaller kid stumbles to the ground as ")
    print("the bigger kid laughs derisively.\n")
    print("You realize you have three choices: ")
    print("  You could [laugh] with the bully, ")
    print("  stay neutral by doing [nothing], ")
    print("  or [help] the victim.\n")
  elif state == "laugh":
    print("You join in laughter at the funny sight. Just then the vice principal ")
    print("walks in and sees you engaged in mocking the smaller kid. She sternly ")
    print("tells you and the other kids who are laughing to stop, and takes your ")
    print("name down to report to your parents. The bigger kid who started this ")
    print("laughs in the vice principal's face and tells her that her ..." )
    print("  You could acknowledge [guilt] and apologize, ")
    print("  or you could [keep laughing] now at the vice principal.\n")
  elif state == "nothing":
    print("You're confused by what you've seen and choose to do nothing.\n")
    print("Just then, your friend behind you in the lunch line sees the ")
    print("kid struggling to get back up in a comical way and bursts out ")
    print("laughing, nudging you mischievously. Do you: ")
    print("  [laugh] with your friend, ")
    print("  or [help] the victim?\n")
  elif state == "help":
    print("The victim thanks you and aks if you want to sit with them at lunch tomorrow.")
  else:
    print("You've fallen into the ether... perhaps you spaced out?")

#ensure movement makes sense
def changeState(state1,state2):
  newstate = state1                 #default
  if state1 == "end" or state1 == "exit":
    print("The situation is over now. You reflect on what just happened.")
    newstate = "end"
  if state1 == "start":             #start
    if state2 == "laugh":
      newstate = "laugh"
    elif state2 == "nothing":
      newstate = "nothing"
    elif state2 == "help":
      newstate = "help"      
  elif state1 == "neutral":         #neutral
    if state2 == "laugh":
      newstate = "laugh"
    elif state2 == "help":
      newstate = "help"
  elif state1 == "laugh":           #laugh
    newstate = "trouble"
  elif state1 == "trouble":         #trouble
    if state2 == "guilt":
      newstate = "guilt"
    elif state2 == "keep laughing": 
      newstate = "trouble"
  elif state1 == "keep laughing":   #keep laughing
    newstate = "resolved"
  else:
    print("You regain your breath; perhaps you spaced out?")
    newstate = state1
  return newstate

#run automatically upon load/F5
if __name__ == "__main__":
  startGame()
