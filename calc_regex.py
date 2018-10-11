#calc_poo

import re
import math

def sub(list):
	result = list[0]
	for i in list[1:]:
		result -= i
	return result

def prod(list):
	result = list[0]
	for i in list[1:]:
		result *= i
	return result

def div(list):
	result = list[0]
	for i in list[1:]:
		if i !=0:
			result /= i
		else:
			result = 'division par zéro impossible'
			break
	return result


def okMarc(chaine):
	motifs = ['^cal', 'som', 'dif', 'prod', 'div', '^mes', 'peri', 'air', 'car', 'cer', 'rec']
	if re.search(motifs[0], chaine, re.IGNORECASE) is not None:
		calcul = '(som|diff|prod|div){1}[A-Za-z]*\s*\d*\.?\d*(\s*(et)?' \
			'\s*\d*\.?\d*)+'
		calc_compile = re.compile(calcul)
		m = calc_compile.search(chaine, re.IGNORECASE)
		nbr = '\d+\.?\d*'
		if m is not None:
			ope = re.findall(nbr, chaine)
			ope = [float(i) for i in ope]
			if re.search(motifs[1], chaine) is not None:
				return sum(ope)
			elif re.search(motifs[2], chaine) is not None:
				return sub(ope)
			elif re.search(motifs[3], chaine) is not None:
				return prod(ope)
			elif re.search(motifs[4], chaine) is not None:
				return div(ope)

		else:
			return "l'opération formulée n'est pas valide"

	elif re.search(motifs[5], chaine) is not None:
		mesure = '(peri|air){1}[A-Za-z]*\s*(car|cer|rec){1}[A-Za-z]*\s*(cot|r|long|lar){1}[A-Za-z]*\s*\d*\.?\d*(\s*(et)?' \
			'((long|lar){1}[A-Za-z]*)?\s*\d+\.?\d*)?'
		mes_compile = re.compile(mesure)
		m = mes_compile.search(chaine, re.IGNORECASE)
		nbr = '\d+\.?\d*'
		if m is not None:
			ope = re.findall(nbr, chaine)
			ope = [float(i) for i in ope]
			if re.search(motifs[6], chaine) is not None:
				if re.search(motifs[8], chaine) is not None:
					return 4*ope[0]
				if re.search(motifs[9], chaine) is not None:
					return 2*math.pi*ope[0]
				if re.search(motifs[10], chaine) is not None:
					if len(ope) == 2:
						return (ope[0]+ope[1])*2
					else:
						return "il faut 2 côtés pour calculer le périmètre d'un rectangle"
			elif re.search(motifs[7], chaine) is not None:
				if re.search(motifs[8], chaine) is not None:
					return ope[0]**2
				if re.search(motifs[9], chaine) is not None:
					return math.pi * ope[0]**2
				if re.search(motifs[10], chaine) is not None:
					if len(ope) == 2:
						return ope[0] * ope[1]
					else:
						"il faut 2 côtés pour calculer l'aire d'un rectangle"
			else:
				return "opération géométrique non implémentée ou non reconnue"

		else:
			return "l'opération formulée n'est pas valide"

	else:
		return "la commande initiale est invalide (rappel: rentrez votre commande en commençant par 'calcul' ou 'mesure'"




