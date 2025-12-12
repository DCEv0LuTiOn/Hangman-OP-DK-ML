'''
Discibtion: This moduls represends the developments of the gui
Creation Date: 11.12.2025
Last Change: 12.12.2025 - wrote nächser_guess funktion, part of spieler_name
Change User: DK
Last Change: 12.12.2025 - added gui.py from old Repo
Change User: DK
Last Change: 11.12.2025 - creation of the gui.py file  
Change User: OP
'''

import os
os.system("cls")

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
       spielende_spieler = []
       spieler = input(f"Bitte geben Sie Ihren Namen an:")
       spielende_spieler.append = spieler
       

def geheimes_wort():
       with open("woerter.txt", encoding="utf-8") as file_of_words:
              pass
              

def nächster_guess():
        while True:
                import re
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
nächster_guess()
#print()
#falscher_guess()
#print()
#gewonnen()
#print()
#verloren()