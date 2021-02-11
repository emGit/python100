from util import macro

def start():
  p0()
  # p1()
  # p2()

def p0():
  macro.moduleStart("Blackjack")
  from util.constants import space
  from util.macro import cls
  import random, art
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  ai_cards = []

  def again():
    if input("Type 'y' to play again\n") == 'y':
      cls()
      player_cards.clear()
      ai_cards.clear()
      play()
    else: exit()

  def deal_card(receiver):
    if receiver == "player":
      player_cards.append(random.choice(cards))
      print(f"You are dealt a card.")
      print(f"You have {player_cards}.")
      if sum(player_cards) == 21:
        print("You win! Your hand is 21, Blackjack!")
        again()
      if sum(player_cards) > 21:
        if 11 in player_cards:
          player_cards.remove(11)
          player_cards.append(1)
        else:
          print("You lose! Your hand is over 21!")
          again()

    elif receiver == "ai":
      ai_cards.append(random.choice(cards))
      print(f"Opponent is dealt a card.")
      if len(ai_cards) == 2:
        print(f"Opponent has [{ai_cards[0]}] and {len(ai_cards) - 1} ? unknown.")
      else: print(f"Opponent has {ai_cards}.")
      if sum(ai_cards) > 21:
        if 11 in ai_cards:
          ai_cards.remove(11)
          ai_cards.append(1)
        else:
          print("You win! Your opponent's hand is over 21!")
          again()

  def end():
    print(space)
    print(f"Your score is {sum(player_cards)}!\n"
          f"Your opponent's score is {sum(ai_cards)}!")
    if sum(ai_cards) > sum(player_cards): print(f"You lose!")
    elif sum(ai_cards) == sum(player_cards): print(f"It is a draw!")
    else: print(f"You win!")
    again()

  def play():
    print(art.logo)
    print("Welcome to blackjack! The aim of the game is to get a higher score \n"
          "than your opponent. If you go over 21 you lose.")

    input("Press Enter to continue...\n")
    deal_card("player")
    deal_card("ai")

    input("Press Enter to continue...\n")
    deal_card("player")
    deal_card("ai")

    if input("Press 'y' if you would like another card... \n") == 'y': deal_card("player")
    if sum(ai_cards) < 17: deal_card("ai")
    end()
  play()

def p1():
  macro.moduleStart("")

def p2():
  macro.moduleStart("")

start()