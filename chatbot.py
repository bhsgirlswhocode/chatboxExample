keepGoing = True

while(keepGoing):
 username = input("Enter your name: ")
 print("Hi, " + username + "! I am Francie. " \
 + "I love studying about women in tech" \
 + " because they inspire me!")

 print()
 birthYear = input("Tell me what year you were born: ")
 print("Did you know know that Intel built the first" \
 + " microprocessor in 1971?")
 print("It happened " + str(int(birthYear) - 1971) \
 + " years before you were born!")

 print()
 annoyingnessLevel = 3
 print("Let me tell you a joke!")
 print("Knock Knock!")
 input("(Say \"Who's there?\") ")
 for num in range(0,annoyingnessLevel):
   print("Banana!")
   input("(Say \"Banana who?\") ")
 print("Orange!")
 input("(Say \"Orange who?\") ")
 print("Orange you glad I didn't say Banana?")
 print("Haha! Isn't that funny?")
 input()

 print()
 info = ""
 while info != "done":
   info = input("Tell me something about yourself, " \
 + username + " (type done to exit): ")
 print("Really? Wow!")
  unanswered = True
 while(unanswered):
   print("Do you want to keep talking? 'yes' or 'no'?")
   answer = input()

   if((answer == "yes") or (answer == "Yes")):
    print("Cool!")
    unanswered = False
   elif((answer == "no") or (answer == "No")):
     print("Oh, byeee")
     keepGoing = False
     unanswered = False
   else:
     print("Huh?")

 print("So what is your favorite color?")
 color = input()

 if((color == "green") or (color == "Green") or (color == "blue") or   (color == "Blue")):
   print("Me too!")
 else:
   print("That's a nice color")
