import eventbrite
import requests
from flask import Flask, url_for
from flask import render_template, redirect, request
from handle_events.handle_calendar import HandleCalendar as HC
from handle_events.handle_events import Events
import json

app = Flask(__name__)

#---------------ouath2 deatils (eventbrite)------------------------------------------#
key = "SIPL2IVAEKK6BOEFS3"
cl_sec = "S7WZZRPSIBMWSMSGERQ65OSBLUKBOXA5ZM7UYSEQTA2PZ7NJLM"
end_point = "http://127.0.0.1:5000/home"






#diff locations on out website


#main route
@app.route('/')
def main():  # put application's code here
    return render_template('login.html', **locals())

@app.route('/auth')
def auth():
    #authorization
    return redirect(f"https://www.eventbrite.com/oauth/authorize?response_type=token&client_id={key}&redirect_uri={end_point}")


@app.route('/home', methods=['GET','POST'])
def view_cal():
    #------------------------------ this code does not work at the moment but can be used for future reference -----------------------------------------------#


    #-------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #post events via button
    if request.method == 'POST':
        HC().add_events()
        print("Events synced")

    return render_template('home.html')





@app.route('/view')
def cal():
    return render_template('view.html')



if __name__ == '__main__':
    app.debug=False
    app.run()
