from flask import Blueprint, request
from datetime import datetime
import json, os, time

internal_api = Blueprint('api_v1', __name__)

@internal_api.route('/getblogpost', methods=['GET'])
def getBlogDatas():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/blogpost.json"))
    with open(path, 'r') as file:
        data = json.load(file)
    return data

@internal_api.route('/createblogpost', methods=['POST'])
def createPostData():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/blogpost.json"))
    with open(path, 'r') as file:
        data = json.load(file)
    
    title = request.form['title']
    subtitle = request.form['subtitle']
    creator = request.form['creator']
    
    formatted_title = title.replace(' ', "-").lower()
    
    nuovo_post = {
        "title": title,
        "formatted_title": formatted_title,
        "subtitle": subtitle,
        "creator": creator,
        "data": str(datetime.fromtimestamp(time.time())), 
    }
    
    data['posts'].append(nuovo_post)
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    
    createPostFile(formatted_title, subtitle)
    
    return "Nuovo post aggiunto con successo", 200
    
def createPostFile(titolo_post, subtitle):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../templates/blogpost/{titolo_post}.html"))
    
    template_html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titolo_post}</title>
    </head>
    <body>
        <h1>{titolo_post}</h1>
        <p>Contenuto del post...</p>
    </body>
    </html>
    """
    
    with open(path, 'w') as file:
        file.write(template_html)
