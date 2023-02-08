from flask import Flask
from requests import request
import json
from flask import Flask
from flask import Flask, request, jsonify,redirect,url_for
import uuid
app = Flask(__name__)
@app.route('/sso/oauth2/authorize',methods=['get'])
def a():
    params = request.args
    client_id = params.get("client_id")
    response_type = params.get("response_type")
    redirect_url  = params.get("redirect_url")
    scope = params.get("scope")
    state = params.get("state")
    if client_id =="123456":
        return
@app.route('/sso/oauth2/token',methods=['post'])
def b():

     data = request.get_data()
     data = json.loads(data)
     grant_type = data.get("grant_type")
     code = data.get("code")
     client_id = data.get("client_id")
     client_secret = data.get("client_secret")
     h = {"accessToken": code}
     if   client_secret =="654321":
         return  h
     return "client_secret is error"