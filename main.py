from flask import Flask,jsonify
import path
import database.user as user

app = Flask(__name__)

@app.route('/')
def api():
    return user.showAllUsers()

configServer = {
    'host':'localhost',
    'port':5000,
    'debug':True
}


app.run(**configServer)
