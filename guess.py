import random
import colorama
from colorama import Fore, Style

colorama.init()

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(Fore.GREEN + Style.BRIGHT + """
 ██████╗  ██████╗  ███████╗ ███╗   ██╗ ███████╗ ██╗   ██╗
██╔════╝ ██╔═══██╗ ██╔════╝ ████╗  ██║ ██╔════╝╚ ██╗ ██╔╝
██║      ██║   ██║ █████╗   ██╔██╗ ██║ █████╗    ╚████╔╝
██║      ██║   ██║ ██╔══╝   ██║╚██╗██║ ██╔══╝    ╚ ██╔╝
╚██████╗ ╚██████╔╝ ███████╗ ██║ ╚████║ ███████╗    ██║
 ╚═════╝ ╚═════╝  ╚══════╝╚═╝  ╚═══╝╚══════╝    ╚═╝
""" + Style.RESET_ALL)

    print(Fore.GREEN + f"Bagels, a deductive logic game.\nI am thinking of a {NUM_DIGITS}-digit number with no repeated digits.\nTry to guess what it is. Here are some clues:\n" + Style.RESET_ALL)
    print(Fore.RED + "When I say: That means:")
    print(Fore.YELLOW + "Pico        One digit is correct but in the wrong position.")
    print(Fore.YELLOW + "Fermi       One digit is correct and in the right position.")
    print(Fore.YELLOW + "Bagels      No digit is correct." + Style.RESET_ALL)

    while True:
        secretNum = getSecretNum()
        print(Fore.GREEN + '\nI have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.' + Style.RESET_ALL)

        guessesTaken = 1
        while guessesTaken <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(Fore.CYAN + f'Guess #{guessesTaken}: ' + Style.RESET_ALL, end='')
                guess = input(Fore.RED + '> ' + Style.RESET_ALL)

            clues = getClues(guess, secretNum)
            print(Fore.YELLOW + clues + Style.RESET_ALL)
            guessesTaken += 1

            if guess == secretNum:
                break
            if guessesTaken > MAX_GUESSES:
                print(Fore.RED + f'You ran out of guesses. The answer was {secretNum}.' + Style.RESET_ALL)
                print('Do you want to play again? (yes or no)')
                if not input(Fore.RED + '> ' + Style.RESET_ALL).lower().startswith('y'):
                    break

    print(Fore.GREEN + 'Thanks for playing!' + Style.RESET_ALL)

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()