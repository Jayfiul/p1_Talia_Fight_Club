from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import json
import requests

app = Flask(__name__) 

#f = open("key_nasa.txt", "r")
#keyNasa = f.read() 
#print(keyNasa) #test to check if the code above gets the key correctly

#response_API = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + keyNasa)
#print(response_API)

#info = response_API.text #pulls all the information from the api file and puts in this string variable
#print(info) #checks out the string of info

#parse_json = json.loads(info) #puts the data into JSON format
#pictureURL = parse_json['url'] #stores the value associated with 'url' in the JSON to variable pictureURL
#print(pictureURL) #checks the image to see it is the correct image

#title = parse_json['title'] #retrieves the title of the picture
#print(title)

@app.route("/") 
def hello_world():
    return render_template('login.html') 

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

