from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from pathlib import Path

# Flask
BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder="static", static_url_path="")
app.secret_key = 'hello'

# Database
DATABASE = "project.db"
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR / DATABASE}"
db.init_app(app)


@app.route('/')
def home():
    args = request.args
    query = args.get('query')
    if query:
        sql_query = text(f"SELECT Name, Category, Price FROM Games "
                         f"WHERE LOWER(Name) LIKE '%{query.lower()}%' AND Released = 1")
        result = db.session.execute(sql_query)
        return render_template("home.html", results=True,
                               query=query, sql_query=sql_query, games=result.fetchall())
    return render_template("home.html", results=False)


@app.route('/reset')
def reset():
    with open('default.sql', mode='r') as f:
        script = f.read().replace("\n", "").replace("\t", "").split(";")
    for line in script:
        print(text(line))
        db.session.execute(text(line))
        db.session.commit()
    flash("Database successfully reset", "success")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
