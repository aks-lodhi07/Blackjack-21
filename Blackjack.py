############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# format of output
# Your cards: [6,10], current score: 16
#     Computer's first card: 10
# Type 'y' to get another card, type 'n' to pass: 
# y
#     Your cards: [6,10,4], current score: 20
#     Computer's first card: 10
# Type 'y' to get another card, type 'n' to pass: 
# n
#    Your final hand: [6,10,4], final score: 20
#    Computer's final hand: [10,9], final score: 19
# You win 😃
# Do you want to play a game of Blackjack? Type 'y' or 'n': 


import random
import os

def deal_card():
     '''Return a random card from the deck'''
# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
     card=random.choice(cards)
     return card
 
def calculate_score(cards):
# Create a function called calculate_score() that takes a List of cards as input and returns the score. 
      if sum(cards)==21 and len(cards)==2:
            return 0
      if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)

      return sum(cards)

def compare(user_score,computer_score):
      if user_score==computer_score:
            return "Draw 🤯"
      elif computer_score==0:
            return "Lose, opponent has Blackjack 🤯"
      elif user_score==0:
            return "Win with a Blackjack 😎"
      elif user_score>21:
            return "You went over, You lose 😭"
      elif computer_score>21:
            return "Opponent went over, You Win 😃"
      elif user_score>computer_score:
            return "You Win 😃"
      else:
            return "You Lose 😭"


def clear():
      os.system('cls' if os.name == 'nt' else 'clear')

def play_blackjack():
      print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      '------'                           |__/           
''')
      user_cards=[]
      computer_cards=[]

      is_game_over=False
      #  Deal the user and computer 2 cards each using deal_card() and append()
      for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

      a=0
      while not is_game_over:     
            user_score=calculate_score(user_cards)
            computer_score=calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score={user_score}")
            print(f"Computer's {a} card is: {computer_cards[a]}")


            if user_score==0 or computer_score==0 or user_score>21:
                  is_game_over=True
            else:
                  other_card=input("Type 'y'(for yes) to et another card, type 'n'(for no) to pass: ")
                  if other_card=='y':
                        a+=1
                        user_cards.append(deal_card())
                  else:
                        is_game_over=True
      while computer_score!=0 and computer_score<17:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)

      print(f"Your final hand is: {user_cards}, final score: {user_score}")
      print(f"Computer's final hand is: {computer_cards}, final score: {computer_score}")

      print(compare(user_score,computer_score))
while input("Do you wnat to play a game of Blackjack? Type 'y' ot 'n': ")=='y':
      clear()
      play_blackjack()