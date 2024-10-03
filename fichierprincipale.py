"""
author : Jean TROUSSIER
date : jeudi 3 octobre
obj :  fichier principale du pendu textuelle
to do :
"""

import tkinter as tk


score = 0
highscore = 0
unsigned_int_live = 0
list_char_lettre_du_mot = []
list_char_lettre_joueur = []
list_char_lettre_joueur_fausse = []
unsigned_int_indicator_victory = 0
as_it_began = False
mot_is = ""

"""
while(1):
    if is_it_the_first_game == True :
        is_it_the_first_game = False
        score = 0
    if as_it_began == True:
        unsigned_int_indicator_victory = mf.void_afficher_mot(unsigned_int_indicator_victory, list_char_lettre_joueur, list_char_lettre_joueur_fausse,list_char_lettre_du_mot)
    if as_it_began == False:
        unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse = mf.initialiser(unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse)
        as_it_began = True
        list_char_lettre_du_mot = mf.list_char_word_seperator(mf.string_word_chooser(mf.list_string_mot("dictionnaire/dico.txt")),list_char_lettre_du_mot)[:]
        mf.list_char_letter_starter(list_char_lettre_du_mot,list_char_lettre_joueur)
    elif mf.bool_death_tester(unsigned_int_live) == True:
        print("vous avez perdu...")
        if highscore < score:
            score == highscore
    elif mf.bool_word_found(unsigned_int_indicator_victory,list_char_lettre_du_mot) == True:
        print("vous avez gagné")
        score += 1
    else :
        char_letter_chosen = input("veuillez entrer une lettre :")
        while mf.bool_is_it_a_char(char_letter_chosen) != True:
            print("la lettre entrée n'est pas valide...")
            char_letter_chosen = input("veuillez entrer une lettre :")
        unsigned_int_live, list_char_lettre_joueur, list_char_lettre_joueur_fausse = mf.void_letter_checker_function(char_letter_chosen,unsigned_int_live,list_char_lettre_joueur,list_char_lettre_du_mot,list_char_lettre_joueur_fausse)
"""

def boutonconfirmer():
    lettre = jean.get()
    print("lettre")
    entry_mot.configure(state= "normal")
    mot_is = lettre

def initializer():
    unsigned_int_live = 0
    list_char_lettre_du_mot = []
    list_char_lettre_joueur = []
    list_char_lettre_joueur_fausse = []
    unsigned_int_indicator_victory = 0

def word_to_print():
    mot_is = ""
    for char_lettre in list_char_lettre_du_mot:
        if char_lettre in list_char_lettre_joueur:
            mot_is += char_lettre
            unsigned_int_indicator_victory += 1
        else:
            mot_is += '_'


def alert():
    print("menubar has been used")






fenetreprinciale =tk.Tk()
menubar = tk.Menu(fenetreprinciale)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="nouveau", command=initializer)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetreprinciale.quit)
menubar.add_cascade(label="Fichier", menu=menu1)


menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)


jean = tk.StringVar()
frame1 = tk.LabelFrame(fenetreprinciale,text='input user')
frame1.pack(side='bottom',padx= 10,pady= 20)
inputuser = tk.Entry(frame1, textvariable=jean)
boutonconfirmer = tk.Button(frame1,text='confirmer',command=boutonconfirmer)
inputuser.pack(side='left')
boutonconfirmer.pack(side='right')
frame2 = tk.LabelFrame(fenetreprinciale,text='mot')
entry_mot = tk.Entry(frame2, textvariable=mot_is)
entry_mot.configure(state="disabled")
entry_mot.pack()
frame2.pack(side='left')
fenetreprinciale.config(menu=menubar)
fenetreprinciale.mainloop()