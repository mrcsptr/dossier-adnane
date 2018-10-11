#flask

from flask import Flask
from calc_regex import *

app = Flask(__name__)


@app.route('/')
def index():
	return 'Bienvenue !'


@app.route('/Marc')
def f():
	return '<h2>le même titre dans le document</h2>'


@app.route('/Tabmult_<a>/')
def tabmult(a):
	a = int(a)
	tabby = list()
	j = 1
	tabby.append("<br>La table de multiplication de %d</br>" % a)
	while j < 11:
		tabby.append("<br>%d * %d = %d</br>" % (a, j, a * j))
		j += 1
	return ''.join(tabby)


@app.route('/facto_<a>/')
def facto(a):
	a = int(a)
	b = 1
	if a >= 0:
		for i in range(1, a+1):
			b *= i
		return "le factoriel de %d est %d" % (a, b)
	else:
		return "c'est pas bien !!"


@app.route('/calc_web/<chaine>')
def calc_web(chaine):
	return str(okMarc(chaine))







if __name__ == '__main__':
	app.run(debug=True)

