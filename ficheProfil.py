#fiche profil

# coding: utf-8

import time
from tkinter import *
from tkinter.messagebox import *
import os
import re
import dbm

def checkformulaire():

	motifs = ['^[A-Z]+((-| ){1}[A-Z]+)*[A-Z]$', '^[A-Z]{1}[a-z]+((-| ){1}[A-Z]{1}[a-z]+)*[a-z]$',
				  '^0\d{1}((-| |\.|_)?\d{2}){4}$', '^[A-Za-z0-9]+([A-Za-z0-9_\.])*@([A-Za-z0-9_\.])+(\.fr)$',
				  '^\d+\s+(rue|avenue|boulevard|impasse){1}\s+[A-Za-z ]+\s+\d{5}\s+[A-Za-z]+$']
	form = [nom.get(), prenom.get(), phone.get(), email.get(), adresse.get()]
	check = [re.search(motifs[i], form[i]) for i in range(0, 5)]


	if not all(check):
		malrempli(check)
	else:
		showinfo('Formulaire rempli', 'Good job!')
		remplissage_fichier(form)


def malrempli(check):
	champ = ['nom', 'prénom', 'téléphone', 'email', 'adresse']
	mal = [champ[i] for i in range(0, 5) if check[i] is None]
	showerror('Erreur', 'champ(s) suivant(s) mal rempli(s):\n-' + '\n-'.join(mal))


def remplissage_fichier(form):
	dbmfile = dbm.open('dbmfile', 'c')
	if 'compteur' in dbmfile:
		dbmfile['compteur'] = str(int(dbmfile['compteur'])+1)
	else:
		dbmfile['compteur'] = str(1)
	if os.path.isfile('Client.fp'):
		fichier = open('Client.fp', 'a')
	else:
		fichier = open('Client.fp', 'w')
	fichier.write("Entrée n° " + str(dbmfile['compteur']) + ":\nDate: " + time.asctime() + "\nNom: " + nom.get() + "\nPrénom: "
			+ prenom.get() + "\nN° tel:" + phone.get() + "\nEmail: " + email.get() + "\nAdresse: " + adresse.get() + "\n")
	fichier.close()
	dbmfile.close()
	fenetre.quit()


fenetre = Tk()

label = Label(fenetre, text="fiche profil", font=72).grid(row=0, column=2, sticky='w', padx=5, pady=5)

label1 = Label(fenetre, text='Nom:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
nom = StringVar()
nom.set("")

LastName = Entry(fenetre, textvariable=nom, width=30).grid(row=1, column=4, sticky='e', padx=5, pady=5)

label2 = Label(fenetre, text="Prénom:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
prenom = StringVar()
prenom.set("")
FirstName = Entry(fenetre, textvariable=prenom, width=30).grid(row=2, column=4, sticky='e', padx=5, pady=5)

label3 = Label(fenetre, text="Tel:").grid(row=3, column=0, sticky='w', padx=5, pady=5)
phone = StringVar()
phone.set("")
Tel = Entry(fenetre, textvariable=phone, width=30).grid(row=3, column=4, sticky='e', padx=5, pady=5)

label4 = Label(fenetre, text="@:").grid(row=4, column=0, sticky='w', padx=5, pady=5)
email = StringVar()
email.set("")
mail = Entry(fenetre, textvariable=email, width=30).grid(row=4, column=4, sticky='e', padx=5, pady=5)

label5 = Label(fenetre, text="adresse:").grid(row=5, column=0, sticky='w', padx=5, pady=5)
adresse = StringVar()
adresse.set("")
snailmail = Entry(fenetre, textvariable=adresse, width=60).grid(row=5, column=4, sticky='e', padx=5, pady=5)


bouton = Button(fenetre, text="Envoyer Formulaire", bg='darkgreen', command=checkformulaire).grid(row=6, column=2, padx=5, pady=5)


fenetre.mainloop()