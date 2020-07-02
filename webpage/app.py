from flask import Flask, render_template, redirect, jsonify
# from flask_pymongo import PyMongo
import spotify
import main 

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html
@app.route("/")
def home():
    return render_template("index.html")

#Route to get input data
@app.route('/', methods = ['POST'])
def input_data():
    track = request.form["song"]
    artist = request.form["artist"]
    return track, artist


# Route for hit_flop
@app.route('/hit_flop/')
def hit_flop():
    track = track
    artist = artist
    
    hit_predict, hit_score = spotify.hit_flop(track, artist)
    return redirect("/", hit_predict=hit_predict, hit_score=hit_score)
   

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/historical/")
def historical():
    return render_template("historical.html")

if __name__ == "__main__":
    app.run(debug=True)