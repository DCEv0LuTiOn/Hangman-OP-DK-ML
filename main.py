'''
Discribtion: This modul is for logical procedures developments  
Creation Date: 11.12.2025
Last Change: OP - 12.12.2025 - creation of the function wort_erzeugen, buchstaben_raten, update_current_guess_progress, check_if_char_in_word_to_guess, check_word_complete, initial_current_guess_progress
Last Change: OP - 11.12.2025 - creation of the main.py file
Change User: OP
'''
import random
import data
import gui
import operator

    #word_to_guess = ""
current_guess_progress = ""
list_of_players = [] 
word_to_guess = ""
error_count = 0
#Hauptprogramm
def main():
    #While --> Loop for the game
    global current_guess_progress
    global list_of_players
    global word_to_guess
    global error_count

    while True:
        current_user_to_guess = 0
        list_of_players = gui.spieler_namen() #Init Players
        wort_erzeugen() # Wort init
        initial_current_guess_progress(word_to_guess) #Init prograss
        error_count = 0

        while True: 
            gui.display_current_user_to_guess(list_of_players[current_user_to_guess])

            match error_count:
                case 0:
                    gui.figur_stage_0()
                case 1:
                    gui.figur_stage_1()
                case 2:
                    gui.figur_stage_2()
                case 3:
                    gui.figur_stage_3()
                case 4:
                    gui.figur_stage_4()
                case 5:
                    gui.figur_stage_5()
        
            buchstaben_raten()

            if check_word_complete() == True:
                gui.display_current_prograss(str.capitalize(current_guess_progress))
                gui.gewonnen()
                break
            elif error_count == 6:
                gui.figur_stage_6()
                gui.verloren()
                break

            #defines who is next to guess
            if current_user_to_guess == len(list_of_players)- 1:
                current_user_to_guess = 0 
            else:
                current_user_to_guess += 1  
                
        if gui.erneutes_spielen() == False:
            break


def wort_erzeugen():
    global word_to_guess 
    #call function, fill list of words
    list_of_words = data.file_read()
    #random selecting word by index
    
    word_to_guess = list_of_words[random.randint(0, len(list_of_words) -1)]
    return  

'''
'''
def buchstaben_raten() -> str: 
    global word_to_guess
    global error_count
    global current_guess_progress
    gui.display_current_prograss(str.capitalize(current_guess_progress))
    guess_user = gui.nächster_guess()

    if len(guess_user) == 1:
        if check_if_char_in_word_to_guess(guess_user) == True:
            update_current_guess_progress(guess_user)
        else:   
            error_count += 1
            gui.falscher_guess()
    else:
        if guess_user == word_to_guess:
           current_guess_progress = guess_user
        else:
            error_count += 1
            gui.falscher_guess()

    return 

'''
Updating the current_guess_progress variable
'''
def update_current_guess_progress(guess_user: str) -> str:
    global current_guess_progress
    global word_to_guess
    char_values_of_word_to_guess = list(word_to_guess)
    char_values_of_current_guess_progress = list(current_guess_progress)

    for i in range(0,len(char_values_of_word_to_guess)):
        if guess_user == char_values_of_word_to_guess[i]:
            char_values_of_current_guess_progress[i] = guess_user
            current_guess_progress = "".join(char_values_of_current_guess_progress)
    return str(char_values_of_current_guess_progress)

'''
Checking if guessed letter is in word_to_guess
'''
def check_if_char_in_word_to_guess(guess: str) -> bool:
    global word_to_guess
    if operator.contains(str.lower(word_to_guess), str.lower(guess)):
        return True
    else: 
        return False
    return

'''
prüft ob das Wort komplett ist
'''
def check_word_complete() -> bool:
    global current_guess_progress
    if operator.contains(current_guess_progress, "_"):
        return False
    else: 
        return True


'''
initialision the current_guess_progress
'''
def initial_current_guess_progress(word_to_guess) -> str:
    global current_guess_progress
    current_guess_progress = ""
    for i in range(0, len(word_to_guess)):
        current_guess_progress += "_" 
    return 


if __name__ == "__main__":
    main()