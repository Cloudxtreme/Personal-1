# all the import

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Load default ocnfig and override config from an environment variable
app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
	"""Connects to the specific database"""
	rv = sqlite.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

@app.cli.command('initdb')
def initdb_command():
	"""Initalizes the database."""
	init_db()
	print('Intialized the database')

def get_db():
	"""Opens a new database connection if there is none yet
	the current application context.
	"""

	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end ofthe request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()
