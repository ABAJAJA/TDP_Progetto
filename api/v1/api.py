from flask import Blueprint, request
from datetime import datetime
from api.utilities import *
import json, os, time, re, random

internal_api = Blueprint('api_v1', __name__)

@internal_api.route('/getMessages', methods=['GET'])
def getMessages():
    if request.headers.get("X-Api-Token") == WEBSERVER_TOKEN:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/messages.json"))
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    else:
        return "Errore, token non valido.", 403

@internal_api.route('/createMessage', methods=['POST'])
def createMessage():
    if request.headers.get("X-Api-Token") == WEBSERVER_TOKEN:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/messages.json"))
        with open(path, 'r') as file:
            data = json.load(file)

        req_data = json.loads(request.data)

        name = req_data['name']
        email = req_data['email']
        phone = req_data['phone']
        message = req_data['message']
        
        newMsg = {
            "name": name,
            "email": email,
            "phone": phone,
            "message": message
        }
        
        data['messages'].append(newMsg)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        
        return "Nuovo messaggio aggiunto con successo", 200
    else:
        return "Errore, token non valido.", 403

@internal_api.route('/getblogpost', methods=['GET'])
def getBlogDatas():
    valid_token = json.loads(TOKENS)
    if request.headers.get("X-Api-Token") in valid_token:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/blogpost.json"))
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    else:
        return "Errore, token non valido.", 403

@internal_api.route('/createblogpost', methods=['POST'])
def createPostData():
    valid_token = json.loads(TOKENS)
    if request.headers.get("X-Api-Token") in valid_token:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../static/logs/blogpost.json"))
        with open(path, 'r') as file:
            data = json.load(file)
        
        title = request.form['title']
        subtitle = request.form['subtitle']
        creator = valid_token[request.headers.get("X-Api-Token")]
        
        formatted_title = sanitize_title(title)
        
        newPost = {
            "title": title,
            "formatted_title": formatted_title,
            "subtitle": subtitle,
            "creator": creator,
            "data": str(datetime.fromtimestamp(time.time()).strftime("%b %d, %Y %T")), 
        }
        
        data['posts'].append(newPost)
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        
        createPostFile(formatted_title, subtitle)
        return "Nuovo post aggiunto con successo", 200
    else:
        return "Errore, token non valido.", 403
    
@internal_api.route("/getcitypollution", methods=["GET"])
def getCityPollution():
    valid_token = json.loads(TOKENS)
    if request.headers.get("X-Api-Token") in valid_token:
        data = {
            "pm10": str(random.randint(15, 50)),
            "pm2_5": str(random.randint(3,25)),
            "NO2": str(random.randint(10, 40)),
        }
        
        return data, 200
    else:
        return "Errore, token non valido.", 403
    
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
    
    template_html = POST_TEMPLATE.replace("%titolo_post%", titolo_post).replace("%sottotitolo_post%", subtitle)
    
    with open(path, 'w') as file:
        file.write(template_html)
