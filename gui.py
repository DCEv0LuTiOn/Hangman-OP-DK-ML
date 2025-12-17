'''
Discibtion: This moduls represends the developments of the gui
Creation Date: 11.12.2025
Last Change: 16.12.2025 - def erneutes Spielen überarbeitet, spieler_namen, gelöscht: erneut_spielen, geheimes_wort
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



def figur_stage_0():
        print("")	
        print("")
        print("")
        print("")
#Figur Stage 1 von 6
def figur_stage_1():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
        print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

#Figur Stage 2 von 6
def figur_stage_2():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
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
                     print("Es können/müssen 2-5 Spieler spielen.")
                     anzahl = int(input(f"Wie viele Spieler spielen mit?:"))
                     if 2 <= anzahl <= 5:
                            pass
                     else:
                            raise               
                except ValueError:
                     print("Bitte geben Sie einen Zahl zwischen 2-5 ein")
                

                if anzahl == 2:
                        name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                        name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                        spieler.append(name_1)
                        spieler.append(name_2)
                        
                elif anzahl == 3:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 3 an:")
                       spieler.append(name_1)
                       spieler.append(name_2)
                       spieler.append(name_3)
                elif anzahl == 4:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 2 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 3 an:")
                       name_4 = input(f"Bitte geben Sie den Namen von Spieler 4 an:")
                       spieler.append(name_1)
                       spieler.append(name_2)
                       spieler.append(name_3)
                       spieler.append(name_4)
                else:
                       name_1 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_2 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_3 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_4 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       name_5 = input(f"Bitte geben Sie den Namen von Spieler 1 an:")
                       spieler.append(name_1)
                       spieler.append(name_2)
                       spieler.append(name_3)
                       spieler.append(name_4)
                       spieler.append(name_5)

                return spieler     
           
def display_current_prograss(current_prograss: str):
       print(f"Erraten Sie folgendes Wort:")
       print(f"{current_prograss}")
       
def nächster_guess() -> str:
        while True:
                guess = input(f"Bitte geben Sie den nächsten Buchstaben ein:")
                if re.fullmatch(r"[A-Za-z]+", guess):
                        print("Ihr geratener Buchstabe / Wort lautet:",guess)
                        break

                else:
                        print("Falsche Eingabe, bitte geben Sie einen Buchstaben ein und keine Zahl oder Sonderzeichen")
                        continue
        return str.lower(guess)
                        

def display_current_user_to_guess(user: str):
       print(f"Hallo {user}, du bist am Zug!")  

def falscher_guess():
       
        

       print("Du hast falsch geraten.")

def gewonnen():
        print("Herzlichen Glückwunsch, du hast Gewonnne \U0001F389\U0001F389\U0001F389")

def verloren():
       print("Du hast verloren \U0001F613\U0001F613\U0001F613")

def erneutes_spielen() -> bool:
        while True:
                auswahl = int(input(f"Was möchten Sie tun?\n1 Um ein Spiel zu starten oder erneut zu Spielen\n2 um das Spiel zu beenden.\nAuswahl:"))
                if auswahl == 1:
                     return True
                else:
                        print("Das Spiel wurde beendent")
                        return False
                      
        
        
 
       
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
#erneutes_spielen()