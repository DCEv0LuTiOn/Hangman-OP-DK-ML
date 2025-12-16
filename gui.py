'''
Discibtion: This moduls represends the developments of the gui
Creation Date: 11.12.2025
Last Change: 16.12.2025 - def erneutes Spielen überarbeitet, spieler_namen bearbeitet
Change User: DK
Last Change: 12.12.2025 - added spieler_namen, erneutes_spielen
Change User: DK
Last Change: 12.12.2025 - written nächser_guess funktion, part of spieler_name
Change User: DK
Last Change: 12.12.2025 - added gui.py from old Repo
Change User: DK
Last Change: 11.12.2025 - creation of the gui.py file  
Change User: OP
'''

import os
import re
import main
os.system("cls")

spiel_neustarten = 1
spiel_beenden = 2


#Figur Stage 1 von 6
def figur_stage_1():
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 2 von 6
def figur_stage_2():
        print("   ",chr(9744),chr(9744),chr(9744))
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 3 von 6
def figur_stage_3():
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("   ",chr(9744),chr(9744),chr(9744))
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 4 von 6
def figur_stage_4():
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("   ",chr(9744),chr(9744),chr(9744))
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 5 von 6
def figur_stage_5():
        print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
        print("     ",chr(9744),"       ",chr(9744))
        print("     ",chr(9744),"       ",chr(9744))
        print("     ",chr(9744),"       ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("     ",chr(9744))
        print("   ",chr(9744),chr(9744),chr(9744))
        print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 6 von 6
def figur_stage_6():
    print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
    print("     ",chr(9744),"       ",chr(9744))
    print("     ",chr(9744),"       ",chr(9744))
    print("     ",chr(9744),"       ",chr(9744))
    print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
    print("     ",chr(9744),"    ",chr(9744),"   ",chr(9744))
    print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
    print("     ",chr(9744),"       ",chr(9744))
    print("     ",chr(9744),"   ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
    print("     ",chr(9744),"       ",chr(9744))
    print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
    print("     ",chr(9744),"     ",chr(9744)," ",chr(9744))	
    print("     ",chr(9744))
    print("   ",chr(9744),chr(9744),chr(9744))
    print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
    print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
    print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Text Prints

def spieler_namen():
       spieler = []
       while True:
                try:
                     anzahl = int(input(f"Wie viele Spieler spielen mit? (2-5)"))
                     if 2 <= anzahl <= 5:
                            break
                     else:
                            print("Bitte ein Zahl zwischen 2 und 5 eingeben.")
                except ValueError:
                     print("Bitte geben Sie eine gültige Zahl ohne Komma an.")
                if anzahl == 2:
                        name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                        name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                elif anzahl == 3:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 3 an:")
                elif anzahl == 4:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 3 an:")
                       name_4 = input(f"Bitte geben Sie den Namen von Spieler 4 an:")
                else:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_4 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_5 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                return name_1,name_2,name_3,name_4,name_5



def geheimes_wort():
        wort_erzeugen()
        gesucht = ""
        x = 0
        länge = len(wort)

        while x < länge:
                gesucht = gesucht + "_"
                x = x+1

        buchstabe = input(f"Eingabe:")

        for eingabe in wort:
                if eingabe == buchstabe:
                        print(eingabe)
                        gesucht[x] = buchstabe
                        x=x+1
    
        print(gesucht)
              
              

def nächster_guess():
        while True:
                guess = input(f"Bitte geben Sie den nächsten Buchstaben ein:")
                if re.fullmatch(r"[A-Za-z]+", guess):
                        print("Ihr geratener Buchstabe / Wort lautet:",guess)
                        break

                else:
                        print("Falsche Eingabe, bitte geben Sie einen Buchstaben ein und keine Zahl oder Sonderzeichen")
                        
       
def falscher_guess():
       
        

       print("Du hast falsch geraten.")

def gewonnen():
        print("Herzlichen Glückwunsch, du hast Gewonnne \U0001F389\U0001F389\U0001F389")

def verloren():
       print("Du hast verloren \U0001F613\U0001F613\U0001F613")

                      
        
        
 
       
#Test
#figur_stage_1()
#print()
#figur_stage_2()
#print()
#figur_stage_3()
#print()
#figur_stage_4()
#print()
#figur_stage_5()
#print()
#figur_stage_6()
#print()
#geheimes_wort()
#print()
#nächster_guess()
#print()
#falscher_guess()
#print()
#gewonnen()
#print()
#verloren()
#print()
#spieler_namen()
#print()
