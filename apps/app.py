from flask import Flask, render_template, redirect, request

def create_app():
    app = Flask(__name__, template_folder="templates")



    @app.route('/')
    def index():
        return render_template('home/index.html', title="Home Page")
    
    @app.route('/about')
    def about():
        return render_template('home/about.html', title="About Page")
    
    return app