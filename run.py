from flask import Flask, render_template
from api.v1.api import internal_api
import json, os

app = Flask(__name__)

app.register_blueprint(internal_api, url_prefix='/api/v1')

@app.route("/")
def index():
    with open("./static/logs/blogpost.json", "r") as file:
        data = json.load(file)
    
    return render_template("index.html", blog_posts=data["posts"])

@app.route("/chi-siamo")
def about():
    return render_template("about.html")

@app.route("/contattaci")
def contattaci():
    return render_template("contact.html")

@app.route("/blogpost/<titolo_post>")
def posts(titolo_post):
    percorso_file_html = os.path.join("blogpost", f"{titolo_post}.html")

    if os.path.exists(percorso_file_html):
        return render_template(percorso_file_html)
    else:
        return render_template("404.html"), 404

@app.errorhandler(404)
def pagina_non_trovata(error):
    return render_template('404.html'), 404


def register_post():
    path = "./templates/blogpost"
    for nome_file in os.listdir(path):
        if nome_file.endswith(".html"):
            titolo_post = os.path.splitext(nome_file)[0]
            app.add_url_rule(f"/blogpost/{titolo_post}.html", endpoint=f"{titolo_post}", view_func=posts)

if __name__ == "__main__":
    register_post()
    app.run(debug=True)
