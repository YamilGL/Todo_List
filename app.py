from flask import Flask, render_template, request

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return render_template('index.html', tasks=tasks)

@app.route('/delete-task', methods=['POST'])
def delete_task():
    task = request.form['task']
    tasks.remove(task)
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)