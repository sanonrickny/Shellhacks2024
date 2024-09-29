from flask import Flask, render_template, request, jsonify
import heapq
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/find_route')
def find_route():
    return render_template('find_route.html')

@app.route('/resource_request')
def resource_request():
    return render_template('resource_request.html')



if __name__ == "__main__":
    app.run(debug=True)
