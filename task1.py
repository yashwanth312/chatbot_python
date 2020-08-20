import pyttsx3
import os
pyttsx3.speak("Welcome to crazy chat bot")

while True :
  p = input("Command me: ")

  if ("notepad" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("notepad")
  elif ("date" in p) :
    os.system("date")
  elif (("www" in p) and (".com" in p)) :
    if ("browse" in p) :
      os.system("chrome" + p[6: ])
    elif ("find" in p) :
      os.system("chrome" + p[4: ])
    elif ("fetch" in p) :
      os.system("chrome" + p[5: ])
  elif ("chrome" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("chrome")
  elif ("putty" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("putty")
  elif ("winscp" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("WinSCP.exe")
  elif ("virtualbox" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("virtualbox")
  elif ("git-bash" in p) and (("launch" in p) or ("run" in p) or ("open" in p)) :
    os.system("git-bash")
  elif ("exit" in p) :
   break
  else :
    print("Command unavailable")