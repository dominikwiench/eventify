from flask import Flask, render_template, request, redirect
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


@app.route('/home')
def index():
    with db.cursor() as cursor:
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        result = cursor.fetchall()
        for record in result:
            print(record)
    return render_template('testdb.html', records=result)


@app.route('/test')
def testing():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        location = request.form['location']
        peopleCount = request.form['peoplecount']
        dater = request.form['dater']
        timer = request.form['timer']

        cur = db.cursor()
        cur.execute("INSERT INTO events(`title`, `description`, `location`, `peoplecount`, `date`, `time`) VALUES(%s, %s, %s, %s, %s, %s)", (title, desc, location, peopleCount, dater, timer))
        db.commit()
        cur.close()

    return redirect('/')


@app.route('/addform')
def addform():
    return render_template('add.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
