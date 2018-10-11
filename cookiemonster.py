#flask

from flask import *
import os
import time

app = Flask(__name__)


def format_ligne(time, addr, plat, browser):
	ligne = "Date: " + time + " IP: " + addr + " OS: " + plat + " Navigateur: " + browser + "\n"
	return ligne

def logging(remote_addr, user_platform, user_browser):
	if os.path.isfile('Log.co'):
		fichier = open('Log.co', 'a')
	else:
		fichier = open('Log.co', 'w')
	ligne = format_ligne(time.asctime(), remote_addr, user_platform, user_browser)
	fichier.write(ligne)
	fichier.close()



@app.route('/')
def index():
	remote_addr = request.remote_addr
	user_platform = request.user_agent.platform
	user_browser = request.user_agent.browser
	logging(remote_addr, user_platform, user_browser)
	return render_template("template_index.html")


@app.route('/journal/')
def journal():
	with open('Log.co', 'r') as fichier:
		return render_template("template_journal.html", lignes=fichier.read().split('\n'))


if __name__ == '__main__':
	app.run(debug=True)



