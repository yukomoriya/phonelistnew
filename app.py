from flask import *
import datetime
from phonelist import save_phonelist, read_phonelist, add_phone, delete_phone
import sqlite3
conn = sqlite3.connect("phone.db", check_same_thread=False)

app = Flask(__name__)

@app.route("/")
def start():
    now = datetime.datetime.now()
    rows =read_phonelist(conn)
    print(rows)
    D = [str(now.year%100), str(now.month), str(now.day)]
    if len(D[1])<2:
        D[1] = '0'+D[1]
    if len(D[2])<2:
        D[2] = '0'+D[2]
    return render_template('list.html', list=rows, date=D)

@app.route("/a")
def second():
    rows =read_phonelist(conn)
    return {"rows":rows}

@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route("/insert")
def insert():
    return render_template('insert.html')




if __name__ == "__main__":
    app.run(debug=True)    