from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# MySQL database conf
db = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='eventify',
)


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
