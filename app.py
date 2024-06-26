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


# @app.route('/')
# def home():
#    return render_template('index.html')


@app.route('/')
def index():
    with db.cursor() as cursor:
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        result = cursor.fetchall()
        # DEV TEST FUNC 
        # for record in result:
        #    print(record)
    return render_template('index.html', records=result)


# Admin Panel
@app.route('/admin')
def adminpanel():
    with db.cursor() as cursor:
        sql = "SELECT * FROM events"
        cursor.execute(sql)
        result = cursor.fetchall()
        # DEV TEST FUNC 
        # for record in result:
        #    print(record)
    return render_template('admin.html', records=result)


# Add form route and render
@app.route('/addform')
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

    return redirect('/admin')


@app.route('/delete/<int:record_id>', methods=['POST'])
def remove(record_id):
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM events WHERE id = %s", (record_id))
        db.commit()
        cursor.close()
    except Exception:
        print("Błąd przy usuwaniu pozycji w panelu")
    return redirect('/admin')


# Edycja dodanego wydarzenia
@app.route('/editform/<int:record_id>', methods=['POST'])
def edit(record_id):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM events WHERE id = %s", (record_id))
        record = cursor.fetchone()
    except Exception:
        print("Błąd przy edycji pozycji w panelu")
    return render_template('edit.html', record=record)


@app.route('/edit/<int:record_id>', methods=['POST'])
def update(record_id):
    title = request.form.get('title')
    desc = request.form.get('desc')
    location = request.form.get('location')
    peoplecount = request.form.get('peoplecount')
    dater = request.form.get('dater')
    timer = request.form.get('timer')

    try:
        cursor = db.cursor()
        cursor.execute("""
            UPDATE events
            SET `title` = %s, `description` = %s, `location` = %s, `peoplecount` = %s,
                       `date` = %s, `time` = %s
            WHERE id = %s
        """, (title, desc, location, peoplecount, dater, timer, record_id))
        db.commit()
        cursor.close()
    except Exception as e:
        print(f"Błąd przy edycji bazy danych: {e}")
    return redirect('/admin')



@app.route('/delete')
def delete():
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
