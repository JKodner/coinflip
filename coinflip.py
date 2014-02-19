import random
coin = ["Heads", "Tails"]
side = random.choice(coin)
turn = 1
while turn < 4:
    print "Turn #" + str(turn)
    print side
    user_side = raw_input("Heads or Tails?")
    if user_side.lower() == "heads" or user_side.lower() == "tails":
        if user_side.lower() == side.lower():
            print "The coin was on " + side + ". You win!"
            break
        elif user_side.lower() != side.lower():
            print "The coin was on " + side + ". You lose."
            turn += 1
    elif user_side.lower() != "heads" and user_side.lower() != "tails":
        print "Please clarify your answer."
