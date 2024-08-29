 #Black jack game
# # 1. your hand should not be greater than 21. if it is higher than 21, you lose.
# # 2. Cards 2-10 are scared using their face value and J,Q,K are all equal to 10
# # 3. Aces can be 1 or 11(You can choose their value)
# # 4. The one who has black jack (Ace + J/q/K), wins.
# # 5. If your score is below 21, the user is asked whether he wants to draw another card.
# # 6. There is no limit to how many cards you want to draw but if your hand gets higher than 21, you lose.
# # 7. if the computer total adds up 16 or lower, it will draw cards till the score is 17 or higher. But if its 17 or higher they stay with their hand.
# # 8. After drawing cards, if the computer busts(total is 21 or higher),user wins.
# # 9. if computer does not busts, then you compare computer score with user score. whoever has a higher total win
#
# #Hints
#
# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/queen/king all amount is 10.
# # The ace can count as 11 or 1.
#
# #cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#
# #Hint create a deal_card() function that uses the list below to "return" a random card.
#
#
import random
from replit import clear
from text import logo


def deal_card():
    "Returns a random card from the deck"
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(users_score,computer_score):
    if users_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, opponent has balckjack!"
    elif users_score == 0:
        return "win with a black jack"
    elif users_score > 21:
        return "you went over. You lose!"
    elif users_score > 21:
        return "opponent went over. you win!"
    elif users_score > computer_score:
        return "you win!"
    else:
        return "you lose!"


user_card = []
computer_cards = []

for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

def game_initialize():
 print(logo)
 user_card = []
 computer_cards = []


for _ in range(2):
        user_card.append(deal_card())
        computer_cards.append(deal_card())

is_game_over = False
while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_cards)

        print(f"your cards: {user_card},current score: {user_score}")
        print(f"computer first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get another card, type 'hold to pass: ")
            if user_should_deal == "hit":
                user_card.append(deal_card())
            else:
                is_game_over = True
                while computer_score != 0 and computer_score:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)


            print(f"your final hand: {user_card}, final score: {user_score}")
            print(f"computer final hand:{computer_cards}, final score: {computer_score}")
            print(compare(user_score, computer_score))





while input("do you want to play a game of blackjack? Type 'Y' or 'n': ") == "y":
    clear()
    game_initialize()
