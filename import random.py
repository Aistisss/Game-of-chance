import random 

num = random.randint(1, 10)
money = 100

#Coin Flip
def random_coin_flip(guess, bet):
  result = random.randint(1,2)

  if bet > money:
      return print("\nYou cannot bet more than your total money")

  if bet <= 0:
      return print("\nYou must bet more than 0")

  print("Playing coin flip!")

  if result == 1:
    print("Coin landed on Heads.")
  elif result == 2:
    print("Coin landed on Tails.")
  

  if guess == "Heads" and result == 1:
    return "You predicted " + str(guess) + " correctly and have WON $" + str(bet) + ", Congratulations on your winnings." + "\nYour new balance is $" + str(money+bet)
  elif guess == "Tails" and result == 2:
    return "You predicted " + str(guess) + ", the coin to land on Tails correctly and have WON $" + str(bet) + ", Congratulations on your winnings." + "\nYour new balance is $" + str(money + bet)

  else:
    return "You predicted " + str(guess) + " incorrectly and have lost $" + str(-bet) + ", better luck next time." + "\nYour new balance is $" + str(money - bet)



#Cho-Han
def cho_han_dice_roll(guess, bet):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  odd_or_even_result = result % 2

  if bet > money:
      return print("\nYou cannot bet more than your total money")

  if bet <= 0:
      return print("\nYou must bet more than 0")
  
  print("\nPlaying cho han!")


  if result % 2 == 0:
    print ("The dice add to CHO (Even).")
  else:
    print ("The dice add to HAN (ODD).")


  if guess == "Even" and odd_or_even_result == 0:
    return "You guessed the result would be EVEN and have WON $" + str(bet) + ", Congratulations on your winnings." + "\nYour new balance is $" + str(money + bet)
  elif guess == "Odd" and odd_or_even_result == 1:
    return "You guessed the result would be odd and have WON $" + str(bet) + ", Congratulations on your winnings." + " \nYour new balance is $" + str(money + bet)
  else:
    return "You guessed " + str(guess) + " and predicted incorrectly, you have now lost $" + str(-bet) + ", better luck next time." + "\nYour new balance is $" + str(money - bet)



#Picking cards game
def picking_cards(guess, bet):
  #Based on the universal 13 card deck (including jack, queen, king, and ace)
  player1 = random.randint(1, 13)
  player2 = random.randint(1, 13)

  if bet > money:
      return print("\nYou cannot bet more than your total money")

  if bet <= 0:
      return print("\nYou must bet more than 0")
  
  print("\nPlaying picking cards!")

  if player1 < player2:
    print("Player 1 drew a higher card than player 2")
  elif player1 > player2:
    print("Player 2 drew a higher card than player 1")
  elif player1 == player2:
    print("Both players drew the same card.") 
    

  if guess == "Player 1" and player1 < player2:
    return "You bet that player 1 would draw a higher card than player 2 and guessed correctly." + "\nYou WON $" + str(bet) + ", Congratulations on your winnings. \nYour new balance is $" + str(money + bet)
  elif guess == "Player 2" and player1 > player2:
    return "You bet that player 2 would draw a higher card than player 1 and guessed correctly." + "\nYou WON $" + str(bet) + ", Congratulations on your winnings. \nYour new balance is $" + str(money + bet)
  elif guess == "Player 1" or "Player 2" and player1 == player2:
    return "Both players drew the same card therefore your bet has been returned back to you to bet again.\nYour balance is $" + str(money)
  else:
    return "You bet that " + str(guess) + " would draw the higher card and guessed incorrectly." + "\nYou lost $" + str(-bet) + ", Better luck next time. \nYour new balance is $" + str(money - bet)



#Playing Roulette
def roulette_game(guess, bet):
  ball_ = random.randint(0, 36)
  even_or_odd_ball = ball_ % 2

  if bet > money:
      return print("\nYou cannot bet more than your total money")

  if bet <= 0:
      return print("\nYou must bet more than 0")

  print("\nPlaying roulette!")

  if guess == "Even" and even_or_odd_ball == 0:
        print("Ball landed on " + str(ball_) + " which is an even number.")
        print("You won $" + str(bet * 2))
        print("Your new balance is $" + str(bet * 2 + money))
        return bet
  elif guess == "Odd" and even_or_odd_ball == 1:
        print("The ball landed on " + str(ball_) + " which is an odd number.")
        print("You won $" + str(bet * 2))
        print("Your new balance is $" + str(bet * 2 + money))
        return bet
        #returning 36 (times the amount of numbers there is to choose from) based on if the player correctly guessed the number
  elif guess == ball_:
        print("The ball landed on " + str(ball_))
        print("You guessed it would land on " + str(guess) + ", and guessed correctly!")
        print("You won $" + str(bet * 36) + "!")
        print("Your new balance is $" + str(bet * 36 + money))
        return bet * 36
  else:
        print("You lost $" + str(bet) + ", Better luck next time.")
        return - 36


#Priting the games
print(random_coin_flip("Heads", 101))
print(cho_han_dice_roll("Odd", 50))
print(picking_cards(5, 50))
print(roulette_game("Even", 10))
print(roulette_game(27, 50))