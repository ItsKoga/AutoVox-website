from flask import Flask, render_template, redirect, request, send_from_directory, url_for, session
import os
from waitress import serve  # pip install waitress
from dotenv import load_dotenv  # pip install python-dotenv

def get_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"      # !! Only in development environment.
    return app

app = get_app()

@app.route("/")
def index():
    context = {
        'title': 'AutoVox',
        'users': 5530,
        'servers': 5,
        'commands': 23
    }
    try:
        return render_template('index.html', **context)
    except Exception as e:
        return str(e)
    
    
@app.route("/invite")
def invite():
    return redirect('https://discord.com/oauth2/authorize?client_id=1281554625744470127&permissions=8&integration_type=0&scope=bot')

@app.route("/support")
def support():
    return redirect('https://discord.gg/8HbjJBGWBd')

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


if __name__ == "__main__":
    print("Autovox is online!")
    serve(app, host="0.0.0.0", port=8000)
    #app.run(debug=True)