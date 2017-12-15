import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from time_input import time_input
from newton import gznewton
from DurationConvexityCalc import DurationCalcwithY, ConvexityCalcwithY

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict( \
	DATABASE=os.path.join(app.root_path, 'flaskr.db'), \
	SECRET_KEY='development key', \
	USERNAME='admin', \
	PASSWORD='default' \
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	"""Opens a new database connection if there is none yet for the
	current application context.
	"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
		db.commit()

@app.cli.command('initdb')
def initdb_command():
	"""Initializes the database."""
	init_db()
	print('Initialized the database.')

@app.route('/')
def show_result():
	return render_template('show_result.html', results=None, error=None)

@app.route('/query', methods=['POST'])
def query():
	error = None
	results = dict()
	m = float(request.form['fv'])
	c = m * float(request.form['cr']) / 100
	timeChange = lambda x:x[-4:] + '/' + x[:-5]
	timeStart = request.form['id']
	timeEnd = request.form['sd']
	timeCurrent = request.form['pd']
	p0 = float(request.form['sp'])
	frequency = int(request.form['pf'])
	p0,m,c,n,t = time_input(m, c, timeStart, timeEnd, timeCurrent, p0, frequency)
	results['y'] = gznewton(p0,c,m,n,t,1.1,0.00001)-1
	results['d'] = DurationCalcwithY(c,m,frequency,n,1.50 / 100,p0)
	results['c'] = ConvexityCalcwithY(c,m,frequency,n,1.50 / 100,p0)
	return render_template('show_result.html', results=results, error=error)

#@app.route('/')
#def show_entries():
#	db = get_db()
#	cur = db.execute('select title, text from entries order by id desc')
#	entries = cur.fetchall()
#	return render_template('show_entries.html', entries=entries)
#
#@app.route('/add', methods=['POST'])
#def add_entry():
#	if not session.get('logged_in'):
#		abort(401)
#	db = get_db()
#	db.execute('insert into entries (title, text) values (?, ?)',  [request.form['title'], request.form['text']])
#	db.commit()
#	flash('New entry was successfully posted')
#	return redirect(url_for('show_entries'))
#
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#	error = None
#	if request.method == 'POST':
#		if request.form['username'] != app.config['USERNAME']:
#			error = 'Invalid username'
#		elif request.form['password'] != app.config['PASSWORD']:
#			error = 'Invalid password'
#		else:
#			session['logged_in'] = True
#			flash('You were logged in')
#			return redirect(url_for('show_entries'))
#	return render_template('login.html', error=error)
#
#@app.route('/logout')
#def logout():
#	session.pop('logged_in', None)
#	flash('You were logged out')
#	return redirect(url_for('show_entries'))
