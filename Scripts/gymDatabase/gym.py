from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == "POST":

        machine = request.form['machine']
        weight = request.form['weight']
        reps = request.form['reps']

        try:
            with sqlite3.connect('gymDatabase.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO workouts(machineNumber,weight,reps) VALUES (?,?,?)",(machine, weight, reps) )
                con.commit()
                msg = "Record added"

                return render_template("result.html", msg = msg)
                con.close()
        except:
            msg = "error"

        finally:
            return render_template('result.html', msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sqlite3.connect('gymDatabase.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from workouts")

    rows = cur.fetchall()
    return render_template('list.html', rows = rows)


if __name__ == "__main__":
    app.run()
