from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog')
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name


@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('blog.html', title="Build A Blog!", tasks=tasks)


@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('newpost.html', title="Add a Blog Entry!",
                           tasks=tasks)


if __name__ == '__main__':
    app.run()
