'''
Discribtion: This modul is for logical procedures developments  
Creation Date: 11.12.2025
Last Change: 11.12.2025 - creation of the main.py file
Change User: OP
'''
import random
import data
import gui
import operator

word_to_guess = ""
current_guess_progress = ""
list_of_players = []


#Hauptprogramm
def main():
    #While --> Loop for the game 
    while True:

        list_of_players = gui.spieler_namen()
        wort_erzeugen()
        initial_current_guess_progress()
    
        break
    pass


def wort_erzeugen():
    #call function, fill list of words
    list_of_words = data.file_read()
    #random selecting word by index
    word_to_guess = list_of_words[random.randint(0, len(list_of_words) -1)]
    return  

'''

'''
def buchstaben_raten() -> str: 
    guess_user = gui.nächster_guess()

    if len(guess_user) == 1:
        pass
    else:
        if guess_user == word_to_guess:
           pass 
        else:
            pass

    return 

'''
Updating the current_guess_progress variable
'''
def update_current_guess_progress(guess_user: str) -> str:
    char_values_of_word_to_guess = str.split(word_to_guess, "")
    char_values_of_current_guess_progress = str.split(current_guess_progress, "")

    for i in range(0,len(char_values_of_word_to_guess)):
        if guess_user == char_values_of_word_to_guess[i]:
            char_values_of_current_guess_progress[i] = guess_user
    return str(char_values_of_current_guess_progress)

'''
Checking if guessed letter is in word_to_guess
'''
def check_if_char_in_word_to_guess(guess: str) -> bool:
    if operator.contains(current_guess_progress, guess):
        return True
    else: 
        return False
    return
'''
prüft ob das Wort komplett ist
'''
def check_word_complete() -> bool:
    if operator.contains(current_guess_progress, "_"):
        return False
    else: 
        return True


'''
initialision the current_guess_progress
'''
def initial_current_guess_progress(word_to_guess) -> str:
    for i in len(word_to_guess):
        current_guess_progress += "_" 
    return 

if __name__ == "__main__":
    main()