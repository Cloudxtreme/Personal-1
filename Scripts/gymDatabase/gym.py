from flask import Flask, render_template, request
import sqlite3

#tuturial comes from
#https://www.tutorialspoint.com/flask/flask_sqlite.htm

app = Flask(__name__)

# The intiial page loaded
@app.route("/")
def main():
    return render_template('main.html')

# The idea is that at the main page you call a different
# url to call the function in this next page.
# it takes the POST data from / and assigns it to variables

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    # This if is not needed really but it checks for data being
    # being transferred by POST

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

# This isn't called from above. But you can access it directly.
# It lists the sqlite data in a table.

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
