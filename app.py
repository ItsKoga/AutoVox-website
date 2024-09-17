from flask import Flask, render_template, redirect, request, send_from_directory, url_for, session
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template
import os
from waitress import serve
from dotenv import load_dotenv 

import database

load_dotenv()

def get_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"      # !! Only in development environment.
    return app

app = get_app()
Mobility(app)

@app.route("/")
@mobile_template('index.html')
def index(template):
    data = database.execute_read_query('SELECT * FROM stats where id = 1')
    context = {
        'title': 'AutoVox',
        'users': f"{data[0][1]:,}",
        'servers': f"{data[0][2]:,}",
        'commands': f"{data[0][3]:,}",
        'request': request
    }
    try:
        return render_template(template, **context)
    except Exception as e:
        return str(e)
    
    
@app.route("/invite")
def invite():
    return redirect('https://discord.com/oauth2/authorize?client_id=1281554625744470127&permissions=8&integration_type=0&scope=bot')

@app.route("/support")
def support():
    return redirect('https://discord.gg/8HbjJBGWBd')

@app.route("/vote")
def vote():
    return redirect('https://top.gg/bot/1281554625744470127/vote')

@app.route("/terms")
def terms():
    context = {
        'title': 'Terms of Service'
    }
    return render_template('terms.html', **context)

@app.route("/privacy")
def privacy():
    context = {
        'title': 'Privacy Policy'
    }
    return render_template('privacy.html', **context)

@app.route("/soon")
def soon():
    context = {
        'title': 'Coming Soon'
    }
    return render_template('soon.html', **context)

@app.route("/docs")
def docs():
    return redirect(url_for('soon'))

@app.route("/status")
def status():
    return redirect(url_for('soon'))

@app.route("/dashboard")
def dashboard():
    return redirect(url_for('soon'))


@app.route("/stats")
def stats():
    stats = database.execute_read_query('SELECT * FROM stats')
    data = {
        'users': stats[0][0],
        'servers': stats[0][1],
        'commands': stats[0][2]
    }
    return data
    


if __name__ == "__main__":
    print("Autovox is online!")
    serve(app, host="0.0.0.0", port=8000)
    #app.run(debug=True)