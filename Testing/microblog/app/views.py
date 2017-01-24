from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Adam'}
	posts = [ #fake posts
		{
			'author': {'nickename': 'john'},
			'body': 'Beautiful day in portland'
		},
		{
			'author': {'nickname': 'susan'},
			'body': 'The avengers were so cool!'
		}
	]

	return render_template('index.html', user=user, posts=posts)
