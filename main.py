from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []


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


app.run()
