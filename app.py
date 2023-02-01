from flask import Flask, render_template, redirect, url_for, flash, request
import flask_login
from flask_login import login_required
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

# User login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    user = User()
    user.id = username
    return user


# Routes
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
    sql_query = text(f"SELECT username from users "
                     f"WHERE username='{username}' AND password=MD5('{password}')")
    result = db.session.execute(sql_query)
    username = result.first()

    if username:
        user = User()
        user.id = username[0]
        flask_login.login_user(user)
        flash(f"Successfully logged in as {username[0]}", "success")
        return redirect(url_for('admin'))

    flash("Incorrect username/password", "danger")
    return render_template("login.html", login_attempt=True, sql_query=sql_query)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash("Successfully logged out", "success")
    return redirect(url_for('home'))


@app.route('/admin')
@login_required
def admin():
    return redirect(url_for('game_list'))


@app.route('/admin/games/list')
@login_required
def game_list():
    sql_exec = text(f"SELECT id, name, category, price, released FROM games")
    results = db.session.execute(sql_exec)
    return render_template("admin/game_list.html", exec=True, sql_exec=sql_exec, games=results)


@app.route('/admin/games/insert', methods=['GET', 'POST'])
@login_required
def game_insert():
    if request.method == "GET":
        return render_template("admin/game_insert.html")

    name = request.form.get('name', '')
    category = request.form.get('category', '')
    price = request.form.get('price', '0')
    released = request.form.get('released', '0')

    sql_exec = text(f"INSERT INTO games (name, category, price, released) VALUES "
                    f"('{name}', '{category}', {price}, {released})")
    db.session.execute(sql_exec)
    db.session.commit()

    flash("Game was successfully added", "success")
    return render_template("admin/game_insert.html", exec=True, sql_exec=sql_exec)


@app.route('/admin/games/update', methods=['GET', 'POST'])
@login_required
def game_update():
    if request.method == "GET":
        return render_template("admin/game_update.html")

    game_id = request.form.get('id', '')
    price = request.form.get('price', '0')

    sql_exec = text(f"UPDATE games SET price={price} "
                    f"WHERE id={game_id}")
    db.session.execute(sql_exec)
    db.session.commit()

    flash("Game was successfully updated", "success")
    return render_template("admin/game_update.html", exec=True, sql_exec=sql_exec)


@app.route('/admin/games/delete', methods=['GET', 'POST'])
@login_required
def game_delete():
    if request.method == "GET":
        return render_template("admin/game_delete.html")

    game_id = request.form.get('id', '')

    sql_exec = text(f"DELETE FROM games WHERE id={game_id}")
    db.session.execute(sql_exec)
    db.session.commit()

    flash("Game was successfully deleted", "success")
    return render_template("admin/game_delete.html", exec=True, sql_exec=sql_exec)


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
