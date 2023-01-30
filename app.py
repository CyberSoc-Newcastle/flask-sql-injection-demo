from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from pathlib import Path

# Flask
BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static", static_url_path="")
app.secret_key = 'hello'

# Database
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost:3306/gamestore"
db.init_app(app)


@app.route('/')
def home():
    args = request.args
    query = args.get('query')
    if query:
        sql_query = text(f"SELECT name, category, price FROM games "
                         f"WHERE LOWER(name) LIKE '%{query.lower()}%' AND released=1")
        result = db.session.execute(sql_query)
        return render_template("home.html", results=True,
                               query=query, sql_query=sql_query, games=result.fetchall())
    return render_template("home.html", results=False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    sql_query = text(f"SELECT username, password from users "
                     f"WHERE username='{username}' AND password=MD5('{password}')")
    result = db.session.execute(sql_query)
    if result.first():
        flash("Login successful", "success")
    else:
        flash("Login failed", "danger")
    return render_template("login.html", login_attempt=True, sql_query=sql_query)


@app.route('/reset')
def reset():
    with open(BASE_DIR / 'db' / 'data.sql', mode='r') as f:
        script = f.read().replace("\n", "").replace("\t", "").split(";")
    for line in script:
        if line == "":
            continue
        db.session.execute(text(line))
        db.session.commit()
    flash("Database successfully reset", "success")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
