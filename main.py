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

def zero():
  print(white + "nothing")
def one():
  print(white + "hotdog")
def two():
  print(white + "e")
def three():
  print(white + "a")
def four():
  print(white + "sports")
def five():
  print(white + "H A M B O U R G E R.")

def quiz_method():
  global score
  global answer 

  print(bright_cyan + "Welcome to the 5 question quiz. answer all the questions correctly to recive: " + green + " H A M B O U R G E R.\n")
  print(bright_blue + "First Question: \n\n")

  answer = input(bright_blue + "Which language is used to make a webpage look good? Is it: \n A. JavaScript,\n B. CSS,\n C. HTML").lower().strip()

  if answer == "a":
    print(red + "Incorrect.")
  elif answer == "c":
    print(red + "Incorrect.")
  elif answer == "b":
    print(green + "Correct!")
    score += 1
    print(bright_blue + "Next Question: \n\n")

    answer = input(bright_blue + "What should you ALWAYS remeber to do before you exit out of your program? Is it: \n A. Throw away your computer,\n B. Run your Code,\n C. Commit and Push to Github. ").lower().strip()

    if answer == "a":
      print(red + "Incorrect.")
    elif answer == "b":
      print(red + "Incorrect.")
    elif answer == "c":
      print(green + "Correct!")
      score += 1
      print(bright_blue + "Next Question: \n\n")

      answer = input(bright_blue + "What is the correct syntax for writing a function in python? is it: \n A. def my_function(): \n B. function myFunction() {} \n C. public void my_Function() { } ").lower().strip()

      if answer == "c":
        print(red + "Incorrect.")
      elif answer == "b":
        print(red + "Incorrect.")
      elif answer == "a":
        score += 1
        print(green + "Correct!")
        print(bright_blue + "Next Question: \n\n")

        answer = input(bright_blue + "Which of the following are used to take user input in python? Is it: \n A. ask() \n B. print() \n C. input() ").lower().strip()

        if answer == "a":
          print(red + "Incorrect.")
        elif answer == "b":
          print(red + "Incorrect.")
        elif answer == "c":
          score += 1
          print(green + "Correct!")
          print(bright_blue + "Last Question: \n\n")

          answer = input(bright_blue + "What is the name of the screen where the questions are being displayed? Is it: \n A. The Console, \n B. IDLE, \n C. The IDE")

          if answer == "a":
            score += 1
            print(green + "Correct!")
          elif answer == "b":
            print(red + "Incorrect.")
          elif answer == "c":
            print(red + "Incorrect.")

  print("\nCongratualtions! You earned " + str(score) + " points!")
  print("\nAnd your prize is: \n\n")

  if score == 0:
    zero()
  elif score == 1:
    one()
  elif score == 2:
    two()
  elif score == 3:
    three()
  elif score == 4:
    four()
  elif score == 5:
    five()



while True:
  quiz_method()

  if score > 0:
    break