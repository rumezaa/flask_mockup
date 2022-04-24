import eventbrite
import requests
from flask import Flask, url_for
from flask import render_template, redirect, request
from handle_events.handle_calendar import HandleCalendar as HC
from handle_events.handle_events import Events
import json

app = Flask(__name__)

key = "SIPL2IVAEKK6BOEFS3"
cl_sec = "S7WZZRPSIBMWSMSGERQ65OSBLUKBOXA5ZM7UYSEQTA2PZ7NJLM"
end_point = "http://127.0.0.1:5000/home"

#static directory keeps our CSS files, img files and js
#app.route represents different endpoints/paths of the website. the / is the root 

@app.route('/')
def main():  # put application's code here
    return render_template('login.html', **locals())

#this handles authentication. /auth is connected to the login form in login.html
@app.route('/auth')
def auth():
    #authorization
    return redirect(f"https://www.eventbrite.com/oauth/authorize?response_type=token&client_id={key}&redirect_uri={end_point}")

#thise is our home page, and it listens for post events
@app.route('/home', methods=['POST'])
def view_cal():
    #------------------------------ this code does not work at the moment but can be used for future reference -----------------------------------------------#
    #getting the query param from url after auth
    code = request.args.get("access_token")
    code = "HMDILKOOYVHWM4HOFU7J"

    data = {"grant_type": "authorization_code",'client_id':key,"client_secret": cl_sec,"code": code,"redirect_uri":end_point}

    header = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    #getting out client id
    cl_id = requests.post('https://www.eventbrite.com/oauth/token',json=data, headers=header)


    try:
        Events.get_events(cl_id)
    except:
        pass

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #post events via button
    if request.method == 'POST':
        HC().add_events()

    return render_template('home.html')




#path for the page where we can view calendar
@app.route('/view')
def cal():
    return render_template('view.html')

#runs the program
if __name__ == '__main__':
    app.debug=False
    app.run()
