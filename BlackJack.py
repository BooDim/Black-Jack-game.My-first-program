from random import choice
from art import logo, firework, game_over, standoff
from replit import clear


# Black Jack game
def black_jack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computers_cards = []
    player_cards = []

    def random_card(who, num):  # Defining a random card
        for _ in range(num):
            chance = choice(cards)
            if chance == 11 and sum(who) > 12:
                who.append(1)
            else:
                who.append(chance)
        return who

    def winner(player, computer):   # Determine the winner
        if player == computer:
            return f'Alas! You have a draw\n{standoff}'
        elif computer > player or player > 21:
            return f'You went over. You lose =(\n{game_over}'
        elif computer < player or computer > 21:
            return f'Congratulation! You`re win!\n{firework}'

    print(f'    ==> Your cards: {random_card(player_cards, 2)}, current score: {sum(player_cards)} <==\n')    # player's starting cards
    random_card(computers_cards, 2)  # Get the starting cards of the computer
    print(f'    Computer`s first card: {computers_cards[0]}\nm')   # Show first computer card

# Player game loop

    action = True
    while action and sum(player_cards) <= 21:
        question = input(f'Type "y" to get another card, type "n" to pass: ')
        if question == 'y':
            random_card(player_cards, 1)
            print(f'    Yor cards: {player_cards}, current score: {sum(player_cards)}')
        else:
            action = False

# Computer game loop

    action_computer = True
    while action_computer and sum(computers_cards) <= 21:
        if sum(computers_cards) < 13:
            random_card(computers_cards, 1)
            print(f'    Computer`s card: {sum(computers_cards)}')
        else:
            print(f'    Computer`s final hand: {computers_cards}, final score: {sum(computers_cards)}')
            action_computer = False

    print(winner(sum(player_cards), sum(computers_cards)))  # Conclusion of the winner on the screen
    ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")   # Continue request
    if ask == 'y':
        black_jack()
        clear()


black_jack()
