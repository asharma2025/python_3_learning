import random

# Declare variables
name = "Joe"
question = "Is it going to rain today?"
answer = ""

# Generating random number
random_number = random.randint(1, 10)

# Using random number to determine answer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Hell no lmao."
else:
  answer = "Error, try again."

# Name string control flow and print
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

# Question string control flow and print
if question == "":
  print("You must ask a question to get an answer!")
else:
  print("Magic 8-Ball's answer: " + answer)