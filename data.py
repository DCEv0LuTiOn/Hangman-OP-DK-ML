'''
Discribtion: Module for import or export Data from third party systems 
Creation Date: 11.12.2025
Last Change: 11.12.2025 - creation of the data.py file and development of the file_read() function.
Change User: OP
'''

def file_read():

    with open("woerter.txt", encoding="utf-8") as file_of_words:
        list_of_words = file_of_words.readlines()

    for i in range(0,len(list_of_words) -1):
        list_of_words[i] = str.replace(list_of_words[i], "\n", "") 
    list_of_words = ["Apel"]
    return list_of_words


liste_test = file_read()
#print(f"{liste_test}")