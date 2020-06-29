
import random
from string import ascii_lowercase

def Main():
    while True:
        menu = input('Type "play" to play the game, "exit" to quit:')
        if menu == "play":
            Play()
        elif menu == "exit":
            break
        else:
            pass
    
def Play():
    words = ['python', 'java', 'kotlin', 'javascript']
    my_word = random.choice(words)
    hint = ['-'] * len(my_word)
    tries = 8
    guesses = set()
    
    print("H A N G M A N")


    while tries > 0:
        print("")
        print("".join(hint))
        char = input("Input a letter:")
        if len(char) > 1:
            print("You should input a single letter")
        elif char in guesses:
            print("You already typed this letter")
    #        tries -= 1
        elif char not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif char in my_word:
            for i in range(len(my_word)):
                if char == my_word[i]:
                    hint[i] = char
    #                if hint == my_word:
    #            print("You survived!")
    #            break
            guesses.add(char)
        else:
            print("No such letter in the word")
            tries -= 1
            guesses.add(char)
    
        if my_word == "".join(hint):
            print(f"You guessed the word {my_word}!")
            print("You survived!")
            break
    else:
        print("You are hanged!")

if __name__ == '__main__':
    Main()
