from flask import Flask, render_template, request
from api.v1.api import internal_api
import json, os, sys

app = Flask(__name__, template_folder='./templates')

app.register_blueprint(internal_api, url_prefix='/api/v1')

@app.route("/")
def home():
    with open("./static/logs/blogpost.json", "r") as file:
        data = json.load(file)
    page = int(request.args.get('page', 1))
    posts_per_page = 10
    start_index = (page - 1) * posts_per_page
    end_index = page * posts_per_page
    paginated_posts = data["posts"][start_index:end_index]

    return render_template("index.html", blog_posts=paginated_posts, next_page=page + 1)

@app.route("/chi-siamo")
def about():
    return render_template("about.html")

@app.route("/contattaci")
def contattaci():
    return render_template("contact.html")

@app.route("/blogpost/<titolo_post>")
def blogpost(titolo_post):
    percorso_file_html = os.path.join("blogpost", f"{titolo_post}.html")

    if os.path.exists(os.path.join(app.template_folder, percorso_file_html)):
        return render_template(f"/blogpost/{titolo_post}.html")
    else:
        return render_template("404.html"), 404

@app.errorhandler(404)
def pagina_non_trovata(error):
    return render_template('404.html'), 404
    
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Il pacchetto {package} non è installato. Installazione in corso...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
if __name__ == "__main__":
    install_package("flask")
    install_package("datetime")    
    app.run(debug=True)
