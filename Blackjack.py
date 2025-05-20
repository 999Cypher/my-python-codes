"""
Blackjack, by 999Cypher courtesy of Python
"""

import random, sys

#constants

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

#Begining of the code

BACKSIDE = 'backside'

def main():
    print(
        '''Blackjack,
        RuLES: Get to as close to 21 without going over.
               Kings, Queens and Jacks are worth 10 points.
               Aces are worth 1 or 11 points.
               Cards 2 to 10 have face value points        
            (H) to take another card
            (S) to stop taking cards
          On first play you can press (D) to double down increasing bet
          If you draw, the bet is returned to the player.
          Dealer stops hitting at 17   
        ''' )

    money = 5000
    while True: #Main game loop
        #Check if player has money
        if money <= 0:
            print('You are broke')
            print('Good thing it is not real money')
            print('Thanks for playing')
            sys.exit()

        #Let player enter bet for round

        print('Money:', money)
        bet = getBet(money)

        #Dealer and player get 2 cards each from deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handle player actions
        print('Bet:', bet)
        while True: #Look until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            #Check if player has bust
            if getHandValues(playerHand) > 21:
                break
            #Get player's move, either H, S or D:
            move = getMove(playerHand, money - bet)

            #Handle players actions
            if move == 'D':
                #Player can increase bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:',bet)

            if move in ('H', 'D'):
                #Takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValues(playerHand) > 21:
                    #Player has busted continue
                    continue

                if move in ('S', 'D'):
                    #Stops player's turn
                    break

            #Handle dealer's actions:
            if getHandValues(playerHand) <= 21:
                while getHandValues(dealerHand) <17:
                    #Dealer hits
                    print('Dealer hits ...')
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)

                    if getHandValues(dealerHand) > 21:
                        break #Dealer has busted

                    input('Press Enter to continue...')
                    print('\n\n')

                #Show final hands
                displayHands(playerHand, dealerHand, True)

                playerValue = getHandValues(playerHand)
                dealerValue = getHandValues(dealerHand)

                #IF player has Won , Lost Or Drawn
                if dealerValue > 21:
                    print('Dealer busts! You win ${}!'.format(bet))
                    money += bet
                elif (playerValue > 21) or (playerValue < dealerValue):
                    print('You Lost!')
                    money -= bet
                elif playerValue > dealerValue:
                    print('You won ${}'.format(bet))
                    money += bet
                elif playerValue == dealerValue:
                    print('You have Drawn ,Bet is returned to you')

                input('Press Enter to continue...')
                print('\n\n')

def getBet(maxBet):
    #Ask player how much they want to place for this round
    while True: #Ask until valid amount is entered
        print('How much do you want to bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue #Ask again if number not entered

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #Player entered valid bet.

def getDeck():
    #Return a list of (rank, suit)  tuples for all 52 cards

    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  #Add numbered cards
        for rank in ('J','Q', 'K', 'A'):
            deck.append((rank, suit))       #Add Face and Ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """ Show the cards, Hide dealer's first card if showDealerHand is False"""
    print()
    if showDealerHand:
        print('DEALER:', getHandValues(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #Hide dealers first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    #show player's cards
    print('PLAYER:',getHandValues(playerHand))
    displayCards(playerHand)

def getHandValues(cards):
    #Returns Values of Card
    value = 0
    numberOfAces = 0

    #Add value of non-ace cards
    for card in cards:
        rank = card[0] #Card is tuple like(rank,suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)

    #Add value for Aces
    value += numberOfAces #Add 1 per ace
    for i in range(numberOfAces):
        #If another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    #Display all cards in the card list.
    rows = ['', '', '', '', ''] #Text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' _____  '
        if card == BACKSIDE:
            #Prints cards back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #Print cards front:
            rank, suit = card #Card is a tuple data structure.

            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    #print each row on the screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """ Asks player for either 'H' for hit, 'S' for stand, 'D' for double down  """
    while True: #Loop until player enters correct move
        #Determine what moves player can make
         moves = ['(H)it', '(S)tand']
    #Player can double down on first move, which we can tell because they'll have exactly 2 cards
         if len(playerHand) == 2 and money > 0:
             moves.append('(D)ouble down')

         #Get player's move:
         movePrompt = ', '.join(moves) + '> '
         move = input(movePrompt).upper()
         if move in ('H', 'S'):
            return move #Player entered valid move
         if move == 'D' and '(D)ouble down' in moves:
            return move #Player entered valid move
#Run the game
if __name__ == '__main__':
    main()















