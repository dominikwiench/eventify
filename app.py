from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def testing():
    return render_template('test.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
