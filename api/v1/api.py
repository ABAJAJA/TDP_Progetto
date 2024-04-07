from flask import Blueprint, request
from datetime import datetime
from api.v1.utilities import *
import json, os, time, re

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
    
    formatted_title = sanitize_title(title)
    
    nuovo_post = {
        "title": title,
        "formatted_title": formatted_title,
        "subtitle": subtitle,
        "creator": creator,
        "data": str(datetime.fromtimestamp(time.time()).strftime("%b %d, %Y %T")), 
    }
    
    data['posts'].append(nuovo_post)
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    
    createPostFile(formatted_title, subtitle)
    
    return "Nuovo post aggiunto con successo", 200
    
def sanitize_title(title):
    # tolgo tutti i caratteri non accettati nei file
    title = title.replace(' ', "-").lower()   
    title = re.sub(r'[àáâãä]', "a'", title)
    title = re.sub(r'[èéêë]', "e'", title)
    title = re.sub(r'[ìíîï]', "i'", title)
    title = re.sub(r'[òóôõö]', "o'", title)
    title = re.sub(r'[ùúûü]', "u'", title)
    title = re.sub(r'[^\w\-\.]', '', title)
    
    return title
    
def createPostFile(titolo_post, subtitle):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../templates/blogpost/{titolo_post}.html"))
    
    template_html = POST_TEMPLATE.replace("%titolo_post%", titolo_post)
    
    with open(path, 'w') as file:
        file.write(template_html)
