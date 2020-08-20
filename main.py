#colors 
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_cyan = "\033[0;96m"
bright_blue = "\033[0;94m"

name = "Mihir"
score = 0
answer = ""

def quiz_method():
  global score
  global answer 

  print(bright_cyan + "Welcome to the 5 question quiz. answer all the questions correctly to recive: " + green + " H a m b u r g e r.\n")
  print(bright_blue + "First Question: \n\n")

  answer = input(bright_blue + "on which show is gordon ramsey the nicest to the competitors? Is it in: \n A. Hell's Kitchen,\n B. MasterChef Junior,\n C. MasterChef.").lower().strip()

  if answer == "a":
    print(red + "Incorrect.")
  elif answer == "c":
    print(red + "Incorrect.")
  elif answer == "b":
    print(green + "Correct!")
    print(bright_blue + "Next Question: \n\n")

    answer = input(bright_blue + "What should you ALWAYS remeber to do before you exit out of your program? Is it: \n A. Throw away your computer,\n B. Run your Code,\n C. Commit and Push to Github.").lower().strip()

    if answer == "a":
      print(red + "Incorrect.")
    elif answer == "b":
      print(red + "Incorrect.")
    elif answer == "c":
      print(green + "Correct!")
      print(bright_blue + "Next Question: \n\n")

      answer = input(bright_blue + "What is the correct syntax for writing a function in python? is it: \n A. def my_function(): \n B. function myFunction() {} \n C. public void my_Function() { } ")

      if answer == "c":
        print(red + "Incorrect.")
      elif answer == "b":
        print(red + "Incorrect.")
      elif answer == "a":
        print(green + "Correct!")
        print(bright_blue + "Next Question: \n\n")

        



quiz_method()