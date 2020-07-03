from flask import Flask, render_template, redirect
import spotify

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html
@app.route("/")
def home():
    return render_template("index.html")

# Route for hit_flop
@app.route('/hit_flop/')
def hit_flop():
    track = track
    artist = artist
    hit_predict, hit_score = spotify.hit_flop(track, artist)
    return redirect("/", hit_predict=hit_predict)

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)