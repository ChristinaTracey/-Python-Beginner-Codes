winning_number=10
number=int(input("Guess the number "))
if number==winning_number:
  print("You WIN")
else:
  if number>winning_number:
    print("Too high")
  else:
    print("Too low")