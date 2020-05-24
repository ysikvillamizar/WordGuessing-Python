"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/ahorcado.jpg'


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
"""INITIAL_GUESSES = 18  """           # Initial number of guesses player starts with


def play_game(secret_word,DEFAULT_FILE): # the funtion send the secret word and the image
    """
    Add your code (remember to delete the "pass" below)
    """
    letter = len(secret_word); #get the length of the word
    INITIAL_GUESSES=len(secret_word)+3; 

    count=0;
    vect = "";
    espacio=letter*'-';
    INITIAL = INITIAL_GUESSES;
    print("The word now looks like this: " + espacio);
    print("You have " + str(INITIAL_GUESSES) + " guesses left");
    image = SimpleImage(DEFAULT_FILE)
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5

    while(count<INITIAL_GUESSES):


        user=str(input("Type a single letter here, then press enter: "))
        user=user.upper();
        if len(user) != 1:
            print("Guess should only be a single character.");

        else:
            if user in secret_word:
                INITIAL = INITIAL - 1;
                for i in range(0,letter,1):
                    list=secret_word[i]


                    if user.upper() in list:

                       print("That guess is correct.")
                       espacio = espacio[:i] + secret_word[i] + espacio[i + 1:]
                       print("The word now looks like this: " + espacio)
                print("You have " + str(INITIAL) + " guesses left");
                count = count + 1;

            else:
                INITIAL=INITIAL-1;
                print("There are no " + user + "'s in the word");
                print("The word now looks like this: " + espacio);
                print("You have " + str(INITIAL) + " guesses left");
                count = count + 1;

        if (espacio == secret_word):
            count=INITIAL_GUESSES;


    if(espacio==secret_word):
          print("You win")
    else:
          print("Sorry, you lost. The secret word was:" + str(secret_word))
          image.show()



def get_word():

    index = random.randrange(10)

    with open('Lexicon.txt', 'r') as file:  # open file for reading
         line=[linea.strip() for linea in file] #remove spaces from words
         word=random.choice(line)               #choose a word
         return word




def main():



    secret_word = get_word() #call to the get_word() funtion
    play_game(secret_word,DEFAULT_FILE) #call to the play_game with the secret word of the funtion and an image


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()