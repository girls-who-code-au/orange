#Call the top-level function:
#> gwcGame()

#top level function
def gwcGame():
  position = "home"
  while position != "sleep":
    printOptions(position)  
    newposition = input("What do you do? : ")    
    position = move(position,newposition)
  
#print options for each location
def printOptions(place):
  if place == "home":
    print("You enter the lunchroom. As you are going to sit at your table, you see the new student, Suzy, trip over her feet. Her lunch flies across the room. A group of students are pointing and laughing. The group leader, Mica, starts making fun of Suzy for being a klutz. What do you do?")
    print("You could [bully]")
  elif place == "bully":
    print("You join in on the bullying, smearing Suzy’s applesauce on the floor as you laugh along with Mica. Suzy seems to be very upset, and after giving her a mean look, she begins to cry. However, this does not go unnoticed by the lunchroom supervisor, who immediately breaks up the situation and sends all of you to the principal’s office. You arrive to cold, disappointed faces. The principal and vice principal sit there, legs and armsfolded, and ask you to explain yourself. Mica says that you two were just playing with Suzy, but the principal denies that blatant lie. Suzy then speaks, and explains that you and Mica tripped her in the lunchroom and smeared her applesauce on the floor, while laughing at her. The principal sighs, and demands that you apologize to Suzy for your actions.")
    print("You can [apologize] or [deny].")
  elif place == "apologize":
    print("You apologize to Suzy for bullying her, and she seems to still be hurt, but accepts your apology. Mica sneers and still insists that she didn’t bully her, and is met with detention and a mandatory meeting with the guidance counselor to discuss the issue further. As you walk away, you gather that you have a long way to go before this action will be fully resolved. You contemplate how the situation could have gone differently…")
    print("To play again, type [home]")
  elif place == "deny":
    print("You insist that you weren’t bullying Suzy, and try to back up Mica’s story. The principal is not having it, and gives you and Mica detention, threatening suspension if the situation is brought to her attention again. She also assigns the two of you to write an essay on bullying, to understand what you’ve done and how it hurts people. As you write this essay in your room, you think about how the situation could have gone differently…")
    print("To play again, type [home]")
  else:
    print("You've fallen into the ether... perhaps you should go to sleep?")

#ensure movement makes sense
def move(place1,place2):
  newplace = place1                                             # default
  if place2 == "sleep":
    newplace = "sleep"
    print("You feel yourself drift off to sleep as you wonder about the adventures you had today and those to come in the future.")
#Movement from Home
  elif place1 == "home":
    if place2 == "home":
      newplace = "home"
    elif place2 == "bully":
      newplace = "bully"
#Movement from Bully
  elif place1 == "bully":
    if place2 == "bully":
      newplace = "bully"
    elif place2 == "apologize":
      newplace = "apologize"
    elif place2 == "deny":
      newplace = "deny"
#Movement from Apologize
  elif place1 == "apologize":
    if place2 == "apologize":
      newplace = "apologize"
    elif place2 == "apologize":
      newplace = "home"
#Movement from Deny
  elif place1 == "deny":
    if place2 == "deny":
      newplace = "deny"
    elif place2 == "deny":
      newplace = "home"
  else:
    print("You've fallen into the ether... perhaps you should go to sleep?")
    newplace = "sleep"
  return newplace
  
#uncomment the automatic main property below to run upon load/F5:
#if __name__ == "__main__":
#  gwcGame()
