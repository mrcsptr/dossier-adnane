#fiche profil web

# coding: utf-8

import os
import re
import dbm
from flask import *


class Fiche_Profil:

	def __init__(self, n, p, t, am, ap):
		self.nom = n
		self.prenom = p
		self.tel = t
		self.mail = am
		self.adresse = ap
		self.ctrlNom = re.compile(r"^[A-Z]+((-| ){1}[A-Z]+)*[A-Z]$")
		self.ctrlPrenom = re.compile(r'^[A-Z]{1}[a-z]+((-| ){1}[A-Z]{1}[a-z]+)*[a-z]$')
		self.ctrlTel = re.compile(r'^0\d{1}((-| |\.|_)?\d{2}){4}$')
		self.ctrlMail = re.compile(r'^[A-Za-z0-9]+([A-Za-z0-9_\.])*@([A-Za-z0-9_\.])+(\.fr)$')
		self.ctrlAdr = re.compile(r'^\d+\s+(rue|avenue|boulevard|impasse){1}\s+[A-Za-z ]+\s+\d{5}\s+[A-Za-z]+$')


	def __repr__(self):
		return "Nom: {} \nPrénom: {} \nTel: {} \n@: {} \nAdresse: {}".format(self.nom, self.prenom, self.tel, self.mail, self.adresse)


	def valNom(self):
		if self.ctrlNom.search(self.nom) is None:
			return False
		else:
			return True

	def valPrenom(self):
		if self.ctrlPrenom.search(self.prenom) is None:
			return False
		else:
			return True

	def valTel(self):
		if self.ctrlTel.search(self.tel) is None:
			return False
		else:
			return True

	def valMail(self):
		if self.ctrlMail.search(self.mail) is None:
			return False
		else:
			return True

	def valAdr(self):
		if self.ctrlAdr.search(self.adresse) is None:
			return False
		else:
			return True

	def isValid(self):
		check = [self.valNom(), self.valPrenom(), self.valTel(), self.valMail(), self.valAdr()]
		if all(check):
			return True
		else:
			return False, check


def malrempli(check):
	champ = {'nom' : 'le nom ne doit comporter que des majuscules', 'prénom':'le prénom doit commencer par une majuscule',
	'téléphone':'le numéro de téléphone doit commencer par un zéro, ne comporter que des chiffres, et faire 10 caractères exactement',
	'email':"l'email doit comporter un arobase, un domaine, etc", 'adresse':"l'adresse doit comporter un numéro, une voie, un code postal et une ville"}
	for i in range(0,5):
		mal_key = list()
		mal_value = list()
		if check[i] is None:
			mal_key.append(list(champ.keys(i)))
			mal_value.append(list(champ.values(i)))

	return mal_key, mal_value


def remplissage_fichier(fp):
	dbmfile = dbm.open('dbmfile', 'c')
	if 'compteur' in dbmfile:
		dbmfile['compteur'] = str(int(dbmfile['compteur'])+1)
	else:
		dbmfile['compteur'] = str(1)
	if os.path.isfile('Client.fp'):
		fichier = open('Client.fp', 'a')
	else:
		fichier = open('Client.fp', 'w')
	fichier.write(fp.__repr__())
	fichier.close()
	dbmfile.close()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.form['nom'] is None:
		return render_template("template_fp.html")
	else:
		fp = Fiche_Profil(request.form['nom'], request.form['prenom'], request.form['tel'], request.form['am'], request.form['ap'])
		test = fp.isValid()
		if len(test) == 1:
			remplissage_fichier(fp)
			return render_template("template_index.html")
		else:
			malrempli(test[1])
			render_template("template_fp.html")


if __name__ == '__main__':
	app.run(debug=True)
