from flask import Flask, url_for
from flask import render_template, redirect, request


app = Flask(__name__)

@app.route('/')
def main():  # put application's code here
    end_point = ""
    return render_template('index.html',**locals())


@app.route('/auth')
def auth():
    key = "SIPL2IVAEKK6BOEFS3"
    return redirect(f"https://www.eventbrite.com/oauth/authorize?response_type=token&client_id={key}&redirect_uri={url_for('home')}")

@app.route('/home', methods=['GET','POST'])
def vew_cal():
    if request.method == 'POST':
        pass

    return render_template('main.html')




if __name__ == '__main__':
    app.debug=False
    app.run()
